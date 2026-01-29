/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.HomeSlider = publicWidget.Widget.extend({
    selector: '.home-hero',
    events: {
        'click .slider-dot-hero': '_onDotClick',
    },

    start: function () {
        this.currentIndex = 0;
        this.images = this.$el.find('.hero-bg-img');
        this.dots = this.$el.find('.slider-dot-hero');
        this.totalImages = this.images.length;
        
        if (this.totalImages > 0) {
            this._startAutoSlide();
        }
    },

    destroy: function () {
        this._stopAutoSlide();
        this._super.apply(this, arguments);
    },

    _startAutoSlide: function () {
        this.interval = setInterval(() => {
            this._nextSlide();
        }, 4000);
    },

    _stopAutoSlide: function () {
        if (this.interval) {
            clearInterval(this.interval);
        }
    },

    _nextSlide: function () {
        this.currentIndex = (this.currentIndex + 1) % this.totalImages;
        this._updateSlide();
    },

    _onDotClick: function (ev) {
        this._stopAutoSlide();
        // Since dots are generated with index in view, we need a way to get index.
        // In the XML I need to ensure dots have an index attribute or we infer it.
        // Let's assume the DOM order matches.
        const $dot = $(ev.currentTarget);
        this.currentIndex = $dot.index();
        this._updateSlide();
        this._startAutoSlide();
    },

    _updateSlide: function () {
        // Toggle active class on images
        this.images.removeClass('active');
        $(this.images[this.currentIndex]).addClass('active');

        // Toggle active class on dots
        this.dots.removeClass('active');
        $(this.dots[this.currentIndex]).addClass('active');
    },
});

publicWidget.registry.StatCounter = publicWidget.Widget.extend({
    selector: '.traction-section-hero',
    
    start: function () {
        this.counters = this.$el.find('.stat-value-hero');
        // Use IntersectionObserver to trigger animation when visible
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this._animateCounters();
                    observer.disconnect();
                }
            });
        }, { threshold: 0.3 });
        
        observer.observe(this.el);
    },

    _animateCounters: function () {
        const duration = 2000; // 2 seconds
        
        this.counters.each((index, el) => {
            const $el = $(el);
            // Ensure value is a string, as jQuery .data() might auto-cast "2" to number 2
            const rawValue = $el.data('value') || $el.text();
            const valueStr = String(rawValue);
            
            // Extract numeric part
            const numericValue = parseInt(valueStr.replace(/[^0-9]/g, '')) || 0;
            const suffix = valueStr.replace(/[0-9.,]/g, ''); // Keep suffixes like "+" or "M+"
            
            // Format check (dots for thousands)
            const useDots = valueStr.includes('.');

            $({ count: 0 }).animate({ count: numericValue }, {
                duration: duration,
                easing: 'swing',
                step: function (now) {
                    const current = Math.floor(now);
                    let formatted = current.toString();
                    if (useDots) {
                        formatted = current.toLocaleString('id-ID');
                    }
                    $el.text(formatted + suffix);
                },
                complete: function () {
                    let formatted = numericValue.toString();
                    if (useDots) {
                        formatted = numericValue.toLocaleString('id-ID');
                    }
                    $el.text(formatted + suffix); // Ensure final value is accurate
                }
            });
        });
    }
});

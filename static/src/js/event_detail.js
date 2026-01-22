/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.EventDetailPage = publicWidget.Widget.extend({
    selector: '#event-detail-page',
    events: {
        'click .tab-button': '_onTabClick',
        'click .contact-button': '_onContactClick',
    },

    start: function () {
        return this._super.apply(this, arguments);
    },

    _onTabClick: function (ev) {
        const $target = $(ev.currentTarget);
        const tabId = $target.data('tab');

        // Update tab buttons
        this.$('.tab-button').removeClass('active');
        $target.addClass('active');

        // Update tab content
        this.$('.tab-content').removeClass('active');
        this.$(`#tab-${tabId}`).addClass('active');
    },

    _onContactClick: function (ev) {
        ev.preventDefault();
        // You can implement a modal or redirect to contact page
        alert('Fitur hubungi panitia akan segera tersedia!');
    }
});

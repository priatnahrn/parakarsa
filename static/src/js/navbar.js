/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.Navbar = publicWidget.Widget.extend({
    selector: '#parakarsa-navbar',
    events: {
        'click #mobile-menu-btn': '_onMobileMenuClick',
        'click #close-mobile-menu': '_onCloseMobileMenu',
        'click .mobile-dropdown-toggle': '_onMobileDropdownToggle',
    },

    _onMobileMenuClick: function (ev) {
        ev.preventDefault();
        const menu = this.$('#mobile-menu');
        menu.removeClass('hidden');
        // Small delay to allow display:block to apply before transition
        setTimeout(() => {
            menu.find('.backdrop').removeClass('opacity-0');
            menu.find('.menu-content').removeClass('-translate-x-full');
        }, 10);
    },

    _onCloseMobileMenu: function (ev) {
        ev.preventDefault();
        const menu = this.$('#mobile-menu');
        menu.find('.backdrop').addClass('opacity-0');
        menu.find('.menu-content').addClass('-translate-x-full');
        
        // Wait for transition to finish before hiding
        setTimeout(() => {
            menu.addClass('hidden');
        }, 300);
    },

    _onMobileDropdownToggle: function (ev) {
        ev.preventDefault();
        const $btn = $(ev.currentTarget);
        const $icon = $btn.find('.dropdown-icon');
        const $target = $btn.next('.mobile-dropdown-content');

        $target.toggleClass('hidden');
        $icon.toggleClass('rotate-180');
    }
});

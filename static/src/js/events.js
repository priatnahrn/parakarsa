/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.EventsPage = publicWidget.Widget.extend({
    selector: '.events-page',
    events: {
        'click .filter-dropdown-trigger': '_onDropdownTriggerClick',
        'click .filter-dropdown-item': '_onDropdownItemClick',
        'click .active-filters .filter-chip button': '_onRemoveFilter',
        'click .clear-all-btn': '_onClearAll',
        'input .search-input': '_onSearchInput',
        'click .pagination-btn:not(.disabled)': '_onPaginationClick',
        'click': '_onDocumentClick',
    },

    start: function () {
        this._super.apply(this, arguments);
        this.searchTimeout = null;
    },

    _onDropdownTriggerClick: function (ev) {
        ev.stopPropagation();
        const dropdown = $(ev.currentTarget).closest('.filter-dropdown');
        
        // Close other dropdowns
        $('.filter-dropdown').not(dropdown).removeClass('open');
        
        // Toggle current
        dropdown.toggleClass('open');
    },

    _onDropdownItemClick: function (ev) {
        ev.stopPropagation();
        const item = $(ev.currentTarget);
        const dropdown = item.closest('.filter-dropdown');
        const filterType = dropdown.data('filter-type'); // category, format, city
        const value = item.data('value');

        dropdown.removeClass('open');
        this._updateUrlParam(filterType, value === 'all' ? null : value);
    },

    _onDocumentClick: function (ev) {
        if (!$(ev.target).closest('.filter-dropdown').length) {
            $('.filter-dropdown').removeClass('open');
        }
    },

    _onRemoveFilter: function (ev) {
        const chip = $(ev.currentTarget).closest('.filter-chip');
        const filterType = chip.data('filter-type');
        this._updateUrlParam(filterType, null); // Remove param
    },

    _onClearAll: function (ev) {
        const url = new URL(window.location.href);
        url.searchParams.delete('category');
        url.searchParams.delete('format');
        url.searchParams.delete('city');
        url.searchParams.delete('search');
        url.searchParams.delete('page');
        window.location.href = url.toString();
    },

    _onSearchInput: function (ev) {
        const query = $(ev.currentTarget).val();
        
        if (this.searchTimeout) {
            clearTimeout(this.searchTimeout);
        }

        this.searchTimeout = setTimeout(() => {
            this._updateUrlParam('search', query || null);
        }, 500); // Debounce 500ms
    },

    _onPaginationClick: function (ev) {
        ev.preventDefault();
        const page = $(ev.currentTarget).data('page');
        if (page) {
            this._updateUrlParam('page', page);
        }
    },

    _updateUrlParam: function (key, value) {
        const url = new URL(window.location.href);
        if (value) {
            url.searchParams.set(key, value);
        } else {
            url.searchParams.delete(key);
        }
        
        // Reset page to 1 on filter change
        if (key !== 'page') {
            url.searchParams.delete('page');
        }

        window.location.href = url.toString();
    }
});

/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.EventsPage = publicWidget.Widget.extend({
    selector: '#events-page',
    events: {
        'click .filter-dropdown-trigger': '_onDropdownClick',
        'click .filter-dropdown-item': '_onDropdownItemClick',
        'click .pagination-btn': '_onPageClick',
        'input #search-input': '_onSearchInput',
        'click #reset-filter-btn': '_onResetFilter',
        'click #clear-all-btn': '_onResetFilter',
        'click .filter-chip button': '_onRemoveChip',
    },

    start: function () {
        this.itemsPerPage = 12;
        this.activeCategory = 'all';
        this.activeStatus = 'all';
        this.activeFormat = 'all';
        this.currentPage = 1;
        this.searchQuery = '';

        this.$eventsContainer = this.$('#events-container');
        this.$paginationControls = this.$('#pagination-controls');
        this.$emptyState = this.$('#empty-state');
        this.$eventCards = this.$('.event-card');
        this.$activeFilters = this.$('#active-filters');
        this.$filterChips = this.$('#filter-chips');

        // Close dropdown when clicking outside
        $(document).on('click', (e) => {
            if (!$(e.target).closest('.filter-dropdown').length) {
                this.$('.filter-dropdown').removeClass('open');
            }
        });

        this._filterEvents();

        return this._super.apply(this, arguments);
    },

    _onDropdownClick: function (ev) {
        ev.stopPropagation();
        const $dropdown = $(ev.currentTarget).closest('.filter-dropdown');
        const isOpen = $dropdown.hasClass('open');
        
        // Close all dropdowns
        this.$('.filter-dropdown').removeClass('open');
        
        // Toggle current
        if (!isOpen) {
            $dropdown.addClass('open');
        }
    },

    _onDropdownItemClick: function (ev) {
        const $item = $(ev.currentTarget);
        const type = $item.data('type');
        const id = $item.data('id');
        const $dropdown = $item.closest('.filter-dropdown');

        // Update selection
        $dropdown.find('.filter-dropdown-item').removeClass('selected');
        $item.addClass('selected');

        // Update trigger text
        const label = $item.find('span').text();
        $dropdown.find('.dropdown-label').text(label);

        // Update trigger active state
        if (id === 'all') {
            $dropdown.find('.filter-dropdown-trigger').removeClass('active');
        } else {
            $dropdown.find('.filter-dropdown-trigger').addClass('active');
        }

        // Close dropdown
        $dropdown.removeClass('open');

        // Apply filter
        if (type === 'category') {
            this.activeCategory = id;
        } else if (type === 'status') {
            this.activeStatus = id;
        } else if (type === 'format') {
            this.activeFormat = id;
        }

        this.currentPage = 1;
        this._filterEvents();
    },

    _onSearchInput: function (ev) {
        this.searchQuery = $(ev.currentTarget).val().toLowerCase();
        this.currentPage = 1;
        this._filterEvents();
    },

    _onResetFilter: function () {
        this.activeCategory = 'all';
        this.activeStatus = 'all';
        this.activeFormat = 'all';
        this.searchQuery = '';
        this.$('#search-input').val('');
        this.currentPage = 1;

        // Reset UI
        this.$('.filter-dropdown-item').removeClass('selected');
        this.$('.filter-dropdown-item[data-id="all"]').addClass('selected');
        this.$('.filter-dropdown-trigger').removeClass('active');
        
        this.$('#category-dropdown .dropdown-label').text('Semua Kategori');
        this.$('#status-dropdown .dropdown-label').text('Semua Status');
        this.$('#format-dropdown .dropdown-label').text('Semua Format');

        this._filterEvents();
    },

    _onRemoveChip: function (ev) {
        const $chip = $(ev.currentTarget).closest('.filter-chip');
        const type = $chip.data('type');

        if (type === 'category') {
            this.activeCategory = 'all';
            this.$('#category-dropdown .filter-dropdown-item').removeClass('selected');
            this.$('#category-dropdown .filter-dropdown-item[data-id="all"]').addClass('selected');
            this.$('#category-dropdown .dropdown-label').text('Semua Kategori');
            this.$('#category-dropdown .filter-dropdown-trigger').removeClass('active');
        } else if (type === 'status') {
            this.activeStatus = 'all';
            this.$('#status-dropdown .filter-dropdown-item').removeClass('selected');
            this.$('#status-dropdown .filter-dropdown-item[data-id="all"]').addClass('selected');
            this.$('#status-dropdown .dropdown-label').text('Semua Status');
            this.$('#status-dropdown .filter-dropdown-trigger').removeClass('active');
        } else if (type === 'format') {
            this.activeFormat = 'all';
            this.$('#format-dropdown .filter-dropdown-item').removeClass('selected');
            this.$('#format-dropdown .filter-dropdown-item[data-id="all"]').addClass('selected');
            this.$('#format-dropdown .dropdown-label').text('Semua Format');
            this.$('#format-dropdown .filter-dropdown-trigger').removeClass('active');
        } else if (type === 'search') {
            this.searchQuery = '';
            this.$('#search-input').val('');
        }

        this.currentPage = 1;
        this._filterEvents();
    },

    _onPageClick: function (ev) {
        const $target = $(ev.currentTarget);
        if ($target.hasClass('disabled')) return;
        
        const page = $target.data('page');
        this.currentPage = page;
        this._renderEvents();
        
        // Scroll to top of list
        document.getElementById('events-grid')?.scrollIntoView({ behavior: 'smooth' });
    },

    _filterEvents: function () {
        const self = this;
        this.filteredEvents = [];

        this.$eventCards.each(function () {
            const $card = $(this);
            const category = $card.data('category');
            const status = $card.data('status');
            const format = $card.data('format');
            const title = ($card.data('title') || '').toString().toLowerCase();

            const categoryMatch = self.activeCategory === 'all' || category === self.activeCategory;
            const statusMatch = self.activeStatus === 'all' || status === self.activeStatus;
            const formatMatch = self.activeFormat === 'all' || format === self.activeFormat;
            const searchMatch = title.includes(self.searchQuery);

            if (categoryMatch && statusMatch && formatMatch && searchMatch) {
                self.filteredEvents.push($card);
            }
        });

        this._updateActiveFilters();
        this._renderEvents();
    },

    _renderEvents: function () {
        // Hide all first
        this.$eventCards.addClass('d-none');
        
        if (this.filteredEvents.length === 0) {
            this.$emptyState.addClass('show');
            this.$paginationControls.addClass('d-none');
            return;
        } else {
            this.$emptyState.removeClass('show');
        }

        // Calculate pagination
        const totalPages = Math.ceil(this.filteredEvents.length / this.itemsPerPage);
        if (this.currentPage > totalPages) this.currentPage = 1;

        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        
        const currentItems = this.filteredEvents.slice(startIndex, endIndex);

        // Show current items
        currentItems.forEach($card => {
            $card.removeClass('d-none');
        });

        this._renderPagination(totalPages);
    },

    _renderPagination: function (totalPages) {
        this.$paginationControls.empty();

        if (totalPages <= 1) {
            this.$paginationControls.addClass('d-none');
            return;
        }

        this.$paginationControls.removeClass('d-none');

        // Prev Button
        const prevDisabled = this.currentPage === 1;
        this.$paginationControls.append(`
            <button class="pagination-btn ${prevDisabled ? 'disabled' : ''}" data-page="${this.currentPage - 1}">
                <i class="fa fa-chevron-left"></i>
            </button>
        `);

        // Page Numbers
        for (let i = 1; i <= totalPages; i++) {
            const isActive = i === this.currentPage;
            this.$paginationControls.append(`
                <button class="pagination-btn ${isActive ? 'active' : ''}" data-page="${i}">
                    ${i}
                </button>
            `);
        }

        // Next Button
        const nextDisabled = this.currentPage === totalPages;
        this.$paginationControls.append(`
            <button class="pagination-btn ${nextDisabled ? 'disabled' : ''}" data-page="${this.currentPage + 1}">
                <i class="fa fa-chevron-right"></i>
            </button>
        `);
    },

    _updateActiveFilters: function () {
        const hasActiveFilters = this.activeCategory !== 'all' || 
                                  this.activeStatus !== 'all' || 
                                  this.activeFormat !== 'all' || 
                                  this.searchQuery !== '';
        
        if (hasActiveFilters) {
            this.$activeFilters.show();
            this.$filterChips.empty();

            if (this.activeCategory !== 'all') {
                const categoryLabel = this.$(`#category-dropdown .filter-dropdown-item[data-id="${this.activeCategory}"] span`).text();
                this.$filterChips.append(`
                    <span class="filter-chip" data-type="category">
                        ${categoryLabel}
                        <button><i class="fa fa-times"></i></button>
                    </span>
                `);
            }

            if (this.activeStatus !== 'all') {
                const statusLabel = this.$(`#status-dropdown .filter-dropdown-item[data-id="${this.activeStatus}"] span`).text();
                this.$filterChips.append(`
                    <span class="filter-chip" data-type="status">
                        ${statusLabel}
                        <button><i class="fa fa-times"></i></button>
                    </span>
                `);
            }

            if (this.activeFormat !== 'all') {
                const formatLabel = this.$(`#format-dropdown .filter-dropdown-item[data-id="${this.activeFormat}"] span`).text();
                this.$filterChips.append(`
                    <span class="filter-chip" data-type="format">
                        ${formatLabel}
                        <button><i class="fa fa-times"></i></button>
                    </span>
                `);
            }

            if (this.searchQuery !== '') {
                this.$filterChips.append(`
                    <span class="filter-chip" data-type="search">
                        "${this.searchQuery}"
                        <button><i class="fa fa-times"></i></button>
                    </span>
                `);
            }
        } else {
            this.$activeFilters.hide();
        }
    }
});

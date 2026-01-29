from odoo import http
from odoo.http import request
import datetime

class ParakarsaWebsite(http.Controller):

    @http.route("/", auth="public", website=True)
    def home(self):
        data = {
            'hero': {
                'images': [
                    "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=2074",
                    "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=2032",
                    "https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=2074"
                ],
                'title': "Orkestrasi Ekonomi Kreatif Masa Depan",
                'subtitle': "Panggungnya Pelaku Ekonomi Kreatif untuk Bertumbuh #Berdampingan #TheNextStageTogether",
            },
            'traction': {
                'stats': [
                    {'value': '5.000+', 'label': 'Pelaku Kreatif'},
                    {'value': '50+', 'label': 'Mitra Kolaborasi'},
                    {'value': '4+', 'label': 'Tahun Pengalaman'},
                    {'value': '2', 'label': 'Kota & Provinsi'},
                ]
            },
            'solution': {
                'title': "Parakarsa tidak hanya mengedukasi. Kami mengorkestrasi.",
                'description': "Sistem Orkestrasi Kinerja Enterprise (OKE)",
                'pillars': [
                    {
                        'id': 1,
                        'title': "Jalur Pertumbuhan Terpandu",
                        'desc': "Leveling & Modular learning path.",
                        'icon_class': "fa fa-search"
                    },
                    {
                        'id': 2,
                        'title': "Koneksi Sistematis",
                        'desc': "Integrasi Hexa-Helix yang solid.",
                        'icon_class': "fa fa-graduation-cap"
                    },
                    {
                        'id': 3,
                        'title': "Experiential Learning",
                        'desc': "Proyek kolaboratif & pengalaman nyata.",
                        'icon_class': "fa fa-line-chart"
                    }
                ]
            },
            'products': [
                {
                    'title': 'Assistancy',
                    'desc': 'Mindset & Growth. Pendampingan intensif untuk membangun fondasi bisnis yang kuat.'
                },
                {
                    'title': 'Agency',
                    'desc': 'Eksekusi & Akselerasi. Layanan profesional untuk mempercepat pertumbuhan bisnis.'
                },
                {
                    'title': 'Advisory',
                    'desc': 'Strategi & Akses Jaringan. Konsultasi'
                }
            ],
            'stories': [
                {
                    'id': 1,
                    'quote': "Parakarsa memberikan ruang kolaborasi yang luar biasa. Saya menemukan partner bisnis baru di sini.",
                    'name': "Andi Wijaya",
                    'role': "Founder",
                    'company': "Startup Kreatif",
                    'image': "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=100"
                },
                {
                    'id': 2,
                    'quote': "Event dan workshop yang diadakan sangat insightful. Skill saya meningkat pesat berkat mentor-mentor hebat.",
                    'name': "Diana Putri",
                    'role': "Desainer Grafis",
                    'company': "Freelance",
                    'image': "https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=100"
                },
                {
                    'id': 3,
                    'quote': "Komunitas yang suportif. Berbagi pengalaman dengan sesama pelaku usaha sangat membantu saya menghadapi tantangan.",
                    'name': "Eko Prasetyo",
                    'role': "Pemilik UMKM",
                    'company': "Snack Lezat",
                    'image': "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=100"
                }
            ]
        }
        return request.render("parakarsa.landing_page", data)

    @http.route('/tentang-kami', auth='public', website=True)
    def about_us(self, **kwargs):
        data = {
            'core_values': [
                {
                    'title': "Kolaboratif",
                    'desc': "Kami percaya perubahan besar lahir dari kerja bersama lintas sektor dan lintas disiplin.",
                    'icon': "fa fa-users"
                },
                {
                    'title': "Berbasis Dampak",
                    'desc': "Setiap program dirancang untuk menghasilkan dampak nyata, bukan sekadar aktivitas seremonial.",
                    'icon': "fa fa-bullseye"
                },
                {
                    'title': "Pembelajaran Aplikatif",
                    'desc': "Belajar melalui praktik nyata, pengalaman langsung, dan simulasi dunia industri.",
                    'icon': "fa fa-bolt"
                },
                {
                    'title': "Inklusif & Berdaya",
                    'desc': "Memberdayakan pelaku kreatif dari berbagai latar belakang agar tumbuh bersama dalam ekosistem yang sehat.",
                    'icon': "fa fa-heart"
                },
                {
                    'title': "Berkelanjutan",
                    'desc': "Mendorong pertumbuhan usaha dan komunitas kreatif yang adaptif dan berjangka panjang.",
                    'icon': "fa fa-layer-group"
                }
            ],
            'team': [
                {'name': "Irfan Fakhri Muhammad, S.Pd", 'role': "CEO-Founder & CEO", 'image': "https://ui-avatars.com/api/?name=Irfan+Fakhri&background=1A4D2E&color=fff&size=512", 'badge': "FOUNDER"},
                {'name': "Khairul Anuar Arifin", 'role': "Advisor & Mentor", 'image': "https://ui-avatars.com/api/?name=Khairul+Anuar&background=E69536&color=fff&size=512", 'badge': "ADVISOR"},
                {'name': "Aditya Kusumaprindana", 'role': "Advisor & Mentor", 'image': "https://ui-avatars.com/api/?name=Aditya+Kusumaprindana&background=E69536&color=fff&size=512", 'badge': "ADVISOR"},
                {'name': "Nur Islami Javad", 'role': "Advisor & Mentor", 'image': "https://ui-avatars.com/api/?name=Nur+Islami&background=E69536&color=fff&size=512", 'badge': "ADVISOR"},
                {'name': "Mutiara Lestari, S.Pd", 'role': "Chief Financial Officer (CFO)", 'image': "https://ui-avatars.com/api/?name=Mutiara+Lestari&background=FCF0DE&color=1A4D2E&size=512", 'badge': "EXECUTIVE"},
                {'name': "Asep Indra Cahyadi", 'role': "Chief Business Development Officer (CBDO)", 'image': "https://ui-avatars.com/api/?name=Asep+Indra&background=FCF0DE&color=1A4D2E&size=512", 'badge': "EXECUTIVE"},
                {'name': "Irpan Alfian", 'role': "Chief Development Officer (CDO)", 'image': "https://ui-avatars.com/api/?name=Irpan+Alfian&background=FCF0DE&color=1A4D2E&size=512", 'badge': "EXECUTIVE"}
            ],
            'history': [
                { 
                    'year': "2016 – 2018", 
                    'title': "Inisiasi & Fondasi",
                    'desc': "Fokus pada inisiasi, pemetaan permasalahan UMKM, dan pembangunan komunitas ekonomi kreatif di Jawa Barat.",
                    'icon': "fa fa-map-marker"
                },
                { 
                    'year': "2019 – 2021", 
                    'title': "Kolaborasi Hexa-Helix",
                    'desc': "Pengembangan metode Theatre of Education serta penguatan kolaborasi lintas sektor melalui pendekatan Hexa-Helix.",
                    'icon': "fa fa-calendar"
                },
                { 
                    'year': "2022 – Sekarang", 
                    'title': "Ekspansi & Dampak",
                    'desc': "Perluasan program pendampingan, inkubasi, dan penguatan ekosistem ekonomi kreatif di tingkat daerah hingga nasional.",
                    'icon': "fa fa-rocket"
                }
            ],
            'missions': [
                "Mengembangkan model pendidikan dan pendampingan yang aplikatif, kolaboratif, dan relevan dengan kebutuhan industri kreatif.",
                "Menghubungkan pelaku ekonomi kreatif dengan pemerintah, akademisi, industri, komunitas, media, dan investor melalui pendekatan Hexa-Helix.",
                "Memperkuat kapasitas pelaku UMKM dan kreator agar mampu beradaptasi, berinovasi, dan berkembang secara berkelanjutan.",
                "Mendorong terbentuknya ekosistem ekonomi kreatif yang terintegrasi dari hulu hingga hilir.",
                "Memberikan dampak nyata bagi pertumbuhan ekonomi kreatif di tingkat daerah hingga nasional."
            ]
        }
        return request.render("parakarsa.about_us_page", data)

    @http.route("/acara", auth="public", website=True)
    def events(self, page=1, search='', category='all', status='all', event_format='all', city='all', **kw):
        images = [
            "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=2070",
            "https://images.unsplash.com/photo-1540575467063-178a50c2df87?q=80&w=2070",
            "https://images.unsplash.com/photo-1511578314322-379afb476865?q=80&w=2069",
            "https://images.unsplash.com/photo-1515187029135-18ee286d815b?q=80&w=2070",
            "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?q=80&w=2012",
            "https://images.unsplash.com/photo-1591115765373-5207764f72e7?q=80&w=2072"
        ]
        
        # Hardcode data for demonstration
        all_events = []
        formats = ['online', 'offline', 'hybrid']
        
        for i in range(30):
            # Create deterministic data
            status_val = 'ongoing' if i < 5 else 'upcoming' if i < 15 else 'finished'
            date_obj = datetime.date.today() + datetime.timedelta(days=(i-5)*2)
            date = date_obj.strftime("%d %b %Y")
            
            cat_val = ["pelatihan", "event", "kolaborasi"][i % 3]
            location = ["Parakarsa Studio, Jakarta", "City Hall, Bandung", "Virtual (Zoom)", "Grand Ballroom, Surabaya"][i % 4]
            # City extraction for filtering simulation
            city_val = "jakarta" if "Jakarta" in location else "bandung" if "Bandung" in location else "surabaya" if "Surabaya" in location else "online"

            fmt_val = formats[i % 3]
            title_base = [
                "Digital Marketing Mastery", "UMKM Creative Fest", "Startup Connect", 
                "Photography Workshop", "Business Strategy Summit", "Community Meetup"
            ][i % 6]
            
            all_events.append({
                'id': i + 1,
                'title': f"{title_base} #{i // 6 + 1}",
                'category': cat_val,
                'status': status_val,
                'format': fmt_val,
                'date': date,
                'time': "09:00 - 15:00 WIB",
                'location': location,
                'city_id': city_val, # For filtering
                'image': images[i % len(images)],
                'organizer': "Parakarsa Academy",
                'price': "Free" if i % 3 == 0 else f"Rp {50 * (i % 4 + 1)}rb",
                'description': "Bergabunglah dalam acara spesial ini yang dirancang untuk meningkatkan keterampilan dan jaringan Anda di dunia industri kreatif."
            })

        # Apply filtering
        events = all_events
        if search:
            events = [e for e in events if search.lower() in e['title'].lower()]
        if category and category != 'all':
            events = [e for e in events if e['category'] == category]
        if status and status != 'all':
            events = [e for e in events if e['status'] == status]
        if event_format and event_format != 'all':
            events = [e for e in events if e['format'] == event_format]
        if city and city != 'all':
             events = [e for e in events if city.lower() in e['location'].lower() or (city == 'online' and e['location'] == 'Virtual (Zoom)')]

        # Pagination logic
        page = int(page)
        ppg = 12
        total = len(events)
        pager = request.website.pager(
            url="/acara",
            total=total,
            page=page,
            step=ppg,
            url_args={
                'search': search,
                'category': category,
                'status': status,
                'event_format': event_format,
                'city': city
            }
        )
        
        # Trim events for the current page
        paged_events = events[(page - 1) * ppg: page * ppg]

        # Group events by status for initial rendering if needed
        ongoing_events = [e for e in paged_events if e['status'] == 'ongoing']
        upcoming_events = [e for e in paged_events if e['status'] == 'upcoming']
        finished_events = [e for e in paged_events if e['status'] == 'finished']

        # Prepare cities for filter
        cities = [
            {'id': 'all', 'label': 'Semua Lokasi'},
            {'id': 'jakarta', 'label': 'Jakarta'},
            {'id': 'bandung', 'label': 'Bandung'},
            {'id': 'surabaya', 'label': 'Surabaya'},
            {'id': 'yogyakarta', 'label': 'Yogyakarta'},
            {'id': 'semarang', 'label': 'Semarang'},
            {'id': 'malang', 'label': 'Malang'},
        ]

        return request.render("parakarsa.events_page", {
            'pager': pager,
            'events': paged_events,
            'ongoing_events': ongoing_events,
            'upcoming_events': upcoming_events,
            'finished_events': finished_events,
            'search_query': search,
            'current_category': category,
            'current_format': event_format,
            'current_status': status,
            'current_city': city,
            'cities': cities,
            'categories': [
                {'id': 'all', 'label': 'Semua Kategori'},
                {'id': 'event', 'label': 'Event'},
                {'id': 'pelatihan', 'label': 'Pelatihan'},
                {'id': 'kolaborasi', 'label': 'Kolaborasi'}
            ],
            'formats': [
                {'id': 'all', 'label': 'Semua Format'},
                {'id': 'online', 'label': 'Online'},
                {'id': 'offline', 'label': 'Offline'},
                {'id': 'hybrid', 'label': 'Hybrid'}
            ]
        })

    @http.route("/acara/<int:event_id>", auth="public", website=True)
    def event_detail(self, event_id):
        images = [
            "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=2070",
            "https://images.unsplash.com/photo-1531058020387-3be344556be6?q=80&w=2070",
            "https://images.unsplash.com/photo-1544531586-fde5298cdd40?q=80&w=2070",
            "https://images.unsplash.com/photo-1516321497487-e288fb19713f?q=80&w=2070",
            "https://images.unsplash.com/photo-1523580494863-6f3031224c94?q=80&w=2070",
            "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?q=80&w=2070"
        ]
        
        # Generate event data (same logic as events list)
        i = event_id - 1
        if i < 0 or i >= 30:
            return request.render("parakarsa.event_detail_page", {'event': None})
        
        status = 'ongoing' if i < 5 else 'upcoming' if i < 15 else 'finished'
        date = "22 Jan 2026" if i < 5 else f"{10 + (i-5)} Feb 2026" if i < 15 else "15 Dec 2025"
        category = ["pelatihan", "event", "kolaborasi"][i % 3]
        location = ["Parakarsa Studio, Jakarta", "City Hall, Bandung", "Virtual (Zoom)", "Grand Ballroom, Surabaya"][i % 4]
        event_format = ['online', 'offline', 'hybrid'][i % 3]
        title_base = [
            "Digital Marketing Mastery", "UMKM Creative Fest", "Startup Connect", 
            "Photography Workshop", "Business Strategy Summit", "Community Meetup"
        ][i % 6]
        
        event = {
            'id': event_id,
            'title': f"{title_base} #{i // 6 + 1}",
            'category': category,
            'status': status,
            'format': event_format,
            'date': date,
            'time': "09:00 - 15:00 WIB",
            'location': location,
            'image': images[i % len(images)],
            'organizer': "Parakarsa Academy",
            'price': "Free" if i % 3 == 0 else f"Rp {50 * (i % 4 + 1)}rb",
            'description': """Bergabunglah dalam acara spesial ini yang dirancang untuk meningkatkan keterampilan dan jaringan Anda di dunia industri kreatif. 

Acara ini akan menghadirkan para pembicara ahli dan praktisi berpengalaman yang siap berbagi insight dan pengalaman mereka. Anda akan mendapatkan kesempatan untuk belajar langsung, berdiskusi, dan membangun koneksi dengan sesama peserta.

Baik Anda seorang pemula yang ingin memulai perjalanan, maupun profesional yang ingin meningkatkan skill, acara ini cocok untuk semua level. Daftarkan diri Anda sekarang dan jadilah bagian dari komunitas yang terus berkembang!""",
            'checklist': [
                "Materi pembelajaran lengkap dalam format digital",
                "Sertifikat resmi setelah menyelesaikan program",
                "Akses ke grup ekklusif peserta dan mentor",
                "Networking dengan profesional dan sesama peserta",
                "Konsultasi gratis pasca acara selama 1 minggu",
                "Rekaman sesi untuk ditonton ulang kapan saja"
            ],
            'rundown': [
                {'time': '08:30 - 09:00', 'activity': 'Registrasi & Welcome Coffee'},
                {'time': '09:00 - 09:30', 'activity': 'Opening Ceremony & Pembukaan'},
                {'time': '09:30 - 10:30', 'activity': 'Sesi 1: Pengenalan & Fundamental'},
                {'time': '10:30 - 10:45', 'activity': 'Coffee Break'},
                {'time': '10:45 - 12:00', 'activity': 'Sesi 2: Deep Dive & Case Study'},
                {'time': '12:00 - 13:00', 'activity': 'Lunch Break & Networking'},
                {'time': '13:00 - 14:30', 'activity': 'Sesi 3: Workshop Praktik'},
                {'time': '14:30 - 15:00', 'activity': 'Q&A, Penutupan & Foto Bersama'}
            ],
            'modules': [
                {
                    'title': 'Pengenalan & Mindset',
                    'items': ['Memahami landasan dan konsep dasar', 'Mindset yang tepat untuk sukses', 'Overview industri terkini']
                },
                {
                    'title': 'Strategi & Perencanaan',
                    'items': ['Menyusun strategi yang efektif', 'Goal setting & action plan', 'Tools dan resource yang dibutuhkan']
                },
                {
                    'title': 'Implementasi & Praktik',
                    'items': ['Hands-on workshop', 'Studi kasus nyata', 'Feedback langsung dari mentor']
                },
                {
                    'title': 'Optimasi & Scale Up',
                    'items': ['Teknik optimasi lanjutan', 'Cara scale up dengan efisien', 'Next steps setelah program']
                }
            ],
            'speakers': [
                {
                    'name': 'Sarah Wijaya',
                    'role': 'Chief Marketing Officer',
                    'company': 'TechGrowth ID',
                    'image': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200'
                },
                {
                    'name': 'Budi Santoso',
                    'role': 'Senior Product Designer',
                    'company': 'Creative Space',
                    'image': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=200'
                },
                {
                    'name': 'Jessica Tan',
                    'role': 'Business Strategist',
                    'company': 'Ventures Cap',
                    'image': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=200'
                }
            ]
        }

        return request.render("parakarsa.event_detail_page", {'event': event})

    # Ecosystem Empty States
    @http.route('/program', auth='public', website=True)
    def program_page(self, **kwargs):
        return request.render("parakarsa.coming_soon_page", {
            'title': 'Program',
            'subtitle': 'Inisiatif Unggulan untuk Mendorong Inovasi',
            'icon_class': 'fa fa-lightbulb-o',
            'heading': 'Program Segera Hadir',
            'description': 'Kami sedang merancang berbagai program inisiatif yang akan mendorong kreativitas dan inovasi di ekosistem kita. Nantikan peluncurannya segera!'
        })

    @http.route('/project', auth='public', website=True)
    def project_page(self, **kwargs):
        return request.render("parakarsa.coming_soon_page", {
            'title': 'Project',
            'subtitle': 'Kolaborasi Nyata dalam Membangun Solusi',
            'icon_class': 'fa fa-handshake-o',
            'heading': 'Project Collaboration',
            'description': 'Ruang kolaborasi untuk proyek-proyek berdampak sedang kami siapkan. Bersiaplah untuk bergabung dalam karya nyata bersama para ahli.'
        })

    @http.route('/product', auth='public', website=True)
    def product_page(self, **kwargs):
        return request.render("parakarsa.coming_soon_page", {
            'title': 'Product',
            'subtitle': 'Produk Berkualitas Karya Komunitas',
            'icon_class': 'fa fa-shopping-bag',
            'heading': 'Katalog Produk Segera Rilis',
            'description': 'Kurasi produk terbaik dari komunitas Parakarsa akan segera hadir di sini. Dukung karya lokal dengan kualitas global.'
        })

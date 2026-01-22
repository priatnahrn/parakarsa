from odoo import http
from odoo.http import request

class ParakarsaWebsite(http.Controller):

    @http.route("/", auth="public", website=True)
    def home(self):
        return request.render("parakarsa.landing_page")

    @http.route("/acara", auth="public", website=True)
    def events(self):
        images = [
            "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=2070",
            "https://images.unsplash.com/photo-1531058020387-3be344556be6?q=80&w=2070",
            "https://images.unsplash.com/photo-1544531586-fde5298cdd40?q=80&w=2070",
            "https://images.unsplash.com/photo-1516321497487-e288fb19713f?q=80&w=2070",
            "https://images.unsplash.com/photo-1523580494863-6f3031224c94?q=80&w=2070",
            "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?q=80&w=2070"
        ]
        
        formats = ['online', 'offline', 'hybrid']
        
        events = []
        for i in range(30):
            status = 'ongoing' if i < 5 else 'upcoming' if i < 15 else 'finished'
            date = "22 Jan 2026" if i < 5 else f"{10 + (i-5)} Feb 2026" if i < 15 else "15 Dec 2025"
            category = ["pelatihan", "event", "kolaborasi"][i % 3]
            location = ["Parakarsa Studio", "City Hall", "Virtual", "Grand Ballroom"][i % 4]
            event_format = formats[i % 3]
            title_base = [
                "Digital Marketing Mastery", "UMKM Creative Fest", "Startup Connect", 
                "Photography Workshop", "Business Strategy Summit", "Community Meetup"
            ][i % 6]
            
            events.append({
                'id': i + 1,
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
                'description': "Bergabunglah dalam acara spesial ini yang dirancang untuk meningkatkan keterampilan dan jaringan Anda di dunia industri kreatif. Dapatkan wawasan langsung dari para ahli dan praktisi terkini."
            })

        # Group events by status
        ongoing_events = [e for e in events if e['status'] == 'ongoing']
        upcoming_events = [e for e in events if e['status'] == 'upcoming']
        finished_events = [e for e in events if e['status'] == 'finished']

        return request.render("parakarsa.events_page", {
            'events': events,
            'ongoing_events': ongoing_events,
            'upcoming_events': upcoming_events,
            'finished_events': finished_events,
            'categories': [
                {'id': 'all', 'label': 'Semua Kategori'},
                {'id': 'event', 'label': 'Event'},
                {'id': 'pelatihan', 'label': 'Pelatihan'},
                {'id': 'kolaborasi', 'label': 'Kolaborasi'}
            ],
            'statuses': [
                {'id': 'all', 'label': 'Semua Status'},
                {'id': 'upcoming', 'label': 'Akan Datang'},
                {'id': 'ongoing', 'label': 'Sedang Berlangsung'},
                {'id': 'finished', 'label': 'Selesai'}
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
        
        formats = ['online', 'offline', 'hybrid']
        
        # Generate event data (same logic as events list)
        i = event_id - 1
        if i < 0 or i >= 30:
            return request.render("parakarsa.event_detail_page", {'event': None})
        
        status = 'ongoing' if i < 5 else 'upcoming' if i < 15 else 'finished'
        date = "22 Jan 2026" if i < 5 else f"{10 + (i-5)} Feb 2026" if i < 15 else "15 Dec 2025"
        category = ["pelatihan", "event", "kolaborasi"][i % 3]
        location = ["Parakarsa Studio, Jakarta", "City Hall, Bandung", "Virtual (Zoom)", "Grand Ballroom, Surabaya"][i % 4]
        event_format = formats[i % 3]
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
                "Akses ke grup eksklusif peserta dan mentor",
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
            ]
        }

        return request.render("parakarsa.event_detail_page", {'event': event})

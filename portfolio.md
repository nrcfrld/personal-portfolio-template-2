# Portfolio

## 1. Taroo

**Taroo** adalah AI landing page builder yang membantu pengguna membuat landing page dengan cepat, sekaligus menghubungkannya langsung ke tools tracking seperti **Meta Pixel** dan **Google Analytics** untuk membaca event yang terjadi di dalam website atau landing page. Situs resminya ada di [taroo.id](https://taroo.id).

### Ringkasan

- **Nama produk:** Taroo
- **Website:** [taroo.id](https://taroo.id)
- **Kategori:** AI landing page builder
- **Fokus utama:** Pembuatan landing page otomatis, event tracking, subscription, dan deployment landing page berbasis subdomain
- **Peran:** Fullstack / product engineering
- **Status:** Portfolio terbaru

### Fitur Utama

- Membuat landing page dengan bantuan AI.
- Menghubungkan landing page langsung dengan **Meta Pixel**.
- Menghubungkan landing page langsung dengan **Google Analytics**.
- Melakukan tracking event di dalam website atau landing page.
- Membuat subdomain secara otomatis untuk setiap landing page.
- Mendukung subscription atau recurring payment.
- Menggunakan dua payment gateway:
  - **Xendit** sebagai payment gateway utama.
  - **Midtrans** sebagai backup payment gateway.

### Arsitektur dan Engineering

- Menggunakan strategi **monorepo** untuk manajemen codebase.
- Deployment sudah menggunakan **CI/CD**.
- Frontend dibangun dengan:
  - **React**
  - **Vite**
  - **Astro**
- Backend dibangun dengan:
  - **NestJS**
- Database menggunakan:
  - **PostgreSQL**

### Tantangan Teknis

- Mengelola recurring payment dan subscription flow.
- Mengintegrasikan dua payment gateway dengan peran berbeda: Xendit sebagai gateway utama dan Midtrans sebagai backup.
- Menangani pembuatan subdomain otomatis untuk landing page.
- Menyusun monorepo agar frontend, backend, dan deployment workflow tetap rapi.
- Menghubungkan tracking event website ke Meta Pixel dan Google Analytics.

### Poin yang Bisa Ditambahkan Nanti

- Link live demo atau domain produk.
- Screenshot landing page builder.
- Contoh landing page yang dihasilkan.
- Detail AI flow: dari prompt sampai landing page jadi.
- Cara sistem membuat dan mengelola subdomain.
- Daftar event tracking yang didukung.
- Detail subscription plan dan payment flow.
- Dampak produk, misalnya jumlah user, landing page yang dibuat, conversion tracking, atau metrik bisnis lain.
- Tanggung jawab spesifik di proyek: backend, frontend, deployment, product design, system design, atau team leadership.

## 2. Colabo

**Colabo** adalah AI project management tools yang membantu project lead memahami kondisi project dari task, komentar, dan aktivitas yang tersebar. Colabo menggunakan AI atau LLM untuk membaca konteks project, membuat summary report, weekly report, serta memungkinkan project lead bertanya langsung tentang kondisi project melalui Telegram atau WhatsApp. Situs resminya ada di [colabo.hecolab.id](https://colabo.hecolab.id).

### Ringkasan

- **Nama produk:** Colabo
- **Website:** [colabo.hecolab.id](https://colabo.hecolab.id)
- **Kategori:** AI project management tools
- **Fokus utama:** Project intelligence, AI reporting, task activity analysis, dan chat-based project assistant
- **Peran:** Fullstack / product engineering
- **Status:** Portfolio project

### Fitur Utama

- Mengelola task, komentar, dan aktivitas project.
- Mengambil konteks project dari task, komentar, dan activity log yang tersebar.
- Menggunakan AI atau LLM untuk membuat summary report.
- Menggunakan AI atau LLM untuk membuat weekly report.
- Mengirimkan laporan mingguan ke **Telegram** atau **WhatsApp**.
- Membuat report dalam format **PDF**.
- Terhubung dengan chat messenger seperti **Telegram** dan **WhatsApp**.
- Memungkinkan project lead berkomunikasi langsung dengan AI melalui chat.
- Mendukung pertanyaan kontekstual seperti status pekerjaan anggota tim, contoh: "Budi lagi mengerjakan apa?"

### Arsitektur dan Engineering

- Frontend dibangun dengan:
  - **React**
  - **Vite**
  - **Bun**
- Backend dibangun dengan:
  - **Go**
  - **Fiber**
- Database menggunakan:
  - **PostgreSQL**
- Deployment sudah menggunakan **CI/CD**.
- CI/CD dijalankan dengan **GitHub Actions**.
- Deployment otomatis diarahkan ke **VPS**.

### Tantangan Teknis

- Mengumpulkan konteks project dari task, komentar, dan aktivitas yang tersebar.
- Merancang AI assistant agar bisa menjawab pertanyaan project lead berdasarkan data project yang relevan.
- Membuat summary dan weekly report yang tetap akurat meskipun data project tersebar di banyak task dan thread komentar.
- Mengintegrasikan AI report dengan Telegram dan WhatsApp.
- Menghasilkan report PDF dari hasil analisis project.
- Menyusun workflow CI/CD dari GitHub Actions ke VPS.
- Menjaga backend Go/Fiber tetap efisien untuk proses scraping, aggregation, dan report generation.

### Poin yang Bisa Ditambahkan Nanti

- Link live demo atau repository.
- Screenshot dashboard project management.
- Contoh weekly report yang dikirim ke Telegram atau WhatsApp.
- Contoh PDF report.
- Detail alur AI: dari scraping activity sampai menghasilkan insight project.
- Detail integrasi WhatsApp dan Telegram.
- Detail permission dan role project lead.
- Daftar jenis pertanyaan yang bisa dijawab oleh AI assistant.
- Dampak produk, misalnya jumlah project yang dikelola, jumlah report yang dibuat, atau waktu yang dihemat untuk project lead.
- Tanggung jawab spesifik di proyek: backend, frontend, AI workflow, chat integration, PDF generation, deployment, atau system design.

## 3. Gkomunika

**Gkomunika** adalah multivendor eSIM order aggregation and auto-fulfillment system untuk bisnis eSIM yang menerima order dari berbagai marketplace dan channel penjualan. Sistem ini mengumpulkan order dari Tokopedia, Shopee, TikTok Shop, dan Shopify, lalu secara otomatis melakukan proses issue eSIM berdasarkan SKU produk dan vendor yang sesuai. Setelah eSIM berhasil diterbitkan, sistem menghasilkan QR Code dan mengirimkannya ke customer melalui email. Situs resminya ada di [gkomunika.com](https://gkomunika.com).

### Ringkasan

- **Nama produk:** Gkomunika
- **Website:** [gkomunika.com](https://gkomunika.com)
- **Kategori:** Multivendor eSIM fulfillment system / marketplace order aggregation platform
- **Fokus utama:** Order aggregation, eSIM auto-issue, marketplace integration, vendor routing, dan QR Code delivery
- **Peran:** Fullstack / integration engineering
- **Status:** Portfolio project

### Fitur Utama

- Mengagregasi order dari beberapa marketplace dan channel penjualan.
- Menerima order dari **Tokopedia**, **Shopee**, dan **TikTok Shop** melalui webhook atau API integration.
- Terhubung dengan **Shopify** sebagai salah satu channel penjualan.
- Menampilkan order dari berbagai channel dalam dashboard order internal.
- Melakukan proses issue eSIM secara otomatis setelah order masuk.
- Menentukan vendor eSIM berdasarkan kode SKU produk.
- Mendukung banyak variasi produk eSIM dari beberapa vendor berbeda.
- Menghasilkan QR Code eSIM setelah proses issue berhasil.
- Mengirimkan QR Code eSIM ke customer melalui email.

### Arsitektur dan Engineering

- Backend dibangun dengan:
  - **Express.js**
  - **Laravel**
- Frontend dibangun dengan:
  - **React**
  - **Vite**
- Terhubung dengan marketplace API dan webhook dari:
  - **Tokopedia**
  - **Shopee**
  - **TikTok Shop**
  - **Shopify**
- Terintegrasi dengan sekitar **tiga vendor eSIM** untuk proses penerbitan produk.

### Tantangan Teknis

- Menjaga sistem tetap stabil dan sustainable meskipun bergantung pada banyak integrasi pihak ketiga.
- Mengelola webhook dan API dari berbagai marketplace dengan format data yang berbeda.
- Menggabungkan order dari beberapa channel penjualan ke dalam satu dashboard internal.
- Menentukan routing vendor berdasarkan SKU produk.
- Menangani proses auto-issue eSIM dari beberapa vendor dengan flow dan API yang berbeda.
- Memastikan QR Code eSIM berhasil dibuat dan dikirimkan ke customer melalui email.
- Menangani kemungkinan kegagalan dari marketplace API, vendor API, email delivery, atau proses issue eSIM.
- Menjaga konsistensi status order dari marketplace sampai eSIM berhasil diterima customer.

### Poin yang Bisa Ditambahkan Nanti

- Link dashboard atau screenshot dashboard order internal.
- Contoh flow order dari marketplace sampai customer menerima QR Code.
- Detail vendor routing berdasarkan SKU.
- Detail retry mechanism atau error handling untuk webhook, vendor API, dan email.
- Jumlah marketplace/channel yang aktif digunakan.
- Jumlah vendor eSIM yang terintegrasi.
- Volume order yang pernah diproses.
- Dampak bisnis, misalnya pengurangan pekerjaan manual, waktu auto-fulfillment, atau peningkatan kecepatan pengiriman eSIM.
- Tanggung jawab spesifik di proyek: backend integration, frontend dashboard, vendor API integration, marketplace webhook, email delivery, atau system reliability.

## 4. Sejawat IDN

**Sejawat IDN** adalah learning management system dan online tryout untuk bimbel kedokteran. Sistem ini dipakai untuk menjual materi belajar, video, dan tryout online melalui [sejawatidn.com](https://sejawatidn.com), dengan arsitektur tiga aplikasi: backend API, frontend end user, dan admin/site owner panel.

### Ringkasan

- **Nama produk:** Sejawat IDN
- **Website:** [sejawatidn.com](https://sejawatidn.com)
- **Kategori:** Learning management system / online tryout platform
- **Fokus utama:** LMS, online tryout, scoring engine, content delivery, dan high-concurrency exam experience
- **Industri:** Bimbel kedokteran
- **Peran:** Fullstack / platform engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan learning management system untuk materi belajar dan video.
- Menyediakan online tryout untuk peserta bimbel kedokteran.
- Menjual materi belajar, video, dan akses tryout.
- Memproses jawaban peserta tryout dengan sistem skor variatif.
- Mendukung pembahasan soal dan hasil tryout di akhir sesi.
- Mendukung pembayaran menggunakan **Midtrans**.
- Memisahkan pengalaman pengguna ke dalam tiga aplikasi:
  - Backend API
  - Frontend end user
  - Admin / site owner panel

### Arsitektur dan Engineering

- Backend API dibangun dengan:
  - **Laravel**
- Database menggunakan:
  - **MySQL**
- Frontend end user dibangun dengan:
  - **Next.js**
  - **React**
- Admin / site owner panel dibangun dengan:
  - **React.js**
  - **Vite**
- Sistem dioptimalkan untuk menangani ribuan user tryout secara bersamaan.

### Tantangan Teknis

- Menangani concurrent user dalam jumlah besar, sekitar **1.000 sampai 2.000 user** secara bersamaan.
- Menjaga website tetap stabil saat traffic tryout sedang tinggi.
- Menjaga performa scoring dan pengiriman data tetap baik saat banyak peserta aktif.
- Mengelola sistem penilaian yang variatif, misalnya:
  - jawaban salah bernilai minus
  - jawaban mendekati benar bernilai lebih tinggi
  - jawaban tertentu bernilai nol
- Melakukan perhitungan skor di akhir tryout.
- Menyajikan pembahasan soal berdasarkan jawaban yang sudah dikerjakan peserta.
- Menjaga pemisahan tanggung jawab antara backend API, frontend end user, dan admin panel.

### Poin yang Bisa Ditambahkan Nanti

- Screenshot halaman tryout, dashboard admin, atau LMS.
- Detail alur peserta dari login, ikut tryout, submit jawaban, sampai hasil keluar.
- Detail mekanisme scoring dan bobot jawaban.
- Detail pembahasan soal dan hasil evaluasi.
- Strategi caching, queueing, atau load handling untuk concurrent user tinggi.
- Volume peserta aktif atau jumlah soal yang pernah diproses.
- Dampak bisnis, misalnya jumlah materi terjual, peserta tryout, atau peningkatan engagement siswa.
- Tanggung jawab spesifik di proyek: backend API, frontend end user, admin panel, scoring engine, performance tuning, atau system design.

## 5. HexSchool

**HexSchool** adalah platform LMS untuk software engineering dan coding. Platform ini menjual course coding, bootcamp, dan private course, sekaligus membutuhkan manajemen konten pembelajaran, materi, sertifikat, dan pembayaran melalui payment gateway. Situs resminya ada di [hexschool.com](https://hexschool.com).

### Ringkasan

- **Nama produk:** HexSchool
- **Website:** [hexschool.com](https://hexschool.com)
- **Kategori:** LMS untuk software engineering
- **Fokus utama:** Course delivery, bootcamp, private course, content management, certificate generation, dan payment processing
- **Peran:** Fullstack / platform engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan LMS untuk pembelajaran coding dan software engineering.
- Menjual course coding, bootcamp, dan private course.
- Mengelola konten pembelajaran dan materi course.
- Menangani pencetakan sertifikat.
- Mendukung pembayaran melalui payment gateway.
- Memisahkan pengalaman pengguna ke dalam frontend user site dan admin site.

### Arsitektur dan Engineering

- Frontend user site dibangun dengan:
  - **Next.js**
- Admin site dibangun dengan:
  - **React**
  - **Vite**
- Backend dibangun dengan:
  - **Laravel**
- Backend berperan sebagai REST API.
- CI/CD menggunakan **Docker**.

### Tantangan Teknis

- Mengelola konten pembelajaran, materi, dan course data dengan rapi.
- Menangani alur pembelian untuk course, bootcamp, dan private course.
- Menghasilkan sertifikat secara konsisten setelah proses belajar atau completion flow selesai.
- Menjaga integrasi payment gateway tetap stabil.
- Memisahkan backend REST API dari frontend user site dan admin site.
- Menjalankan deployment dengan Docker agar workflow CI/CD tetap repeatable.

### Poin yang Bisa Ditambahkan Nanti

- Link dashboard admin atau screenshot LMS.
- Detail alur pembelian course sampai akses belajar aktif.
- Detail certificate generation flow.
- Detail payment gateway yang digunakan.
- Detail struktur konten pembelajaran dan modul course.
- Volume siswa atau course yang aktif.
- Dampak bisnis, misalnya jumlah enrollment, completion rate, atau sertifikat yang diterbitkan.
- Tanggung jawab spesifik di proyek: backend API, frontend user site, admin site, certificate generation, payment integration, atau deployment.

## 6. Kelas Drafter

**Kelas Drafter** adalah platform LMS untuk bidang arsitektur yang menjual bootcamp online, online course video, dan materi pembelajaran. Sistem ini mendukung pembayaran melalui Midtrans dan menggunakan arsitektur frontend user site, admin dashboard, serta backend REST API. Situs resminya ada di [kelasdrafter.id](https://www.kelasdrafter.id/).

### Ringkasan

- **Nama produk:** Kelas Drafter
- **Website:** [kelasdrafter.id](https://www.kelasdrafter.id/)
- **Kategori:** LMS untuk arsitektur
- **Fokus utama:** Online course, bootcamp online, content delivery, dan payment processing
- **Peran:** Fullstack / platform engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan LMS untuk pembelajaran bidang arsitektur.
- Menjual bootcamp online.
- Menjual online course video dan materi pembelajaran.
- Mendukung pembayaran melalui **Midtrans**.
- Memisahkan pengalaman pengguna ke dalam frontend user site dan admin dashboard.

### Arsitektur dan Engineering

- Frontend user site dibangun dengan:
  - **Next.js**
- Admin site dibangun dengan:
  - **React.js**
- Backend dibangun dengan:
  - **Laravel REST API**
- Database menggunakan:
  - **MySQL**

### Tantangan Teknis

- Mengelola course, materi, dan konten pembelajaran dengan struktur yang rapi.
- Menangani alur pembelian dan akses konten setelah pembayaran berhasil.
- Menjaga integrasi Midtrans tetap stabil.
- Memisahkan backend API dari frontend user site dan admin dashboard.
- Menjaga konsistensi data antara user experience, payment status, dan content access.

### Poin yang Bisa Ditambahkan Nanti

- Link dashboard admin atau screenshot LMS.
- Detail alur pembelian bootcamp atau course.
- Detail struktur materi belajar dan video.
- Detail payment flow dengan Midtrans.
- Volume user atau enrollment yang aktif.
- Dampak bisnis, misalnya jumlah peserta kursus atau completion rate.
- Tanggung jawab spesifik di proyek: backend API, frontend user site, admin dashboard, payment integration, atau content management.

## 7. DokterGPT

**DokterGPT** adalah AI assistant untuk dokter yang membantu kegiatan harian dokter melalui WhatsApp. Assistant ini dapat dipakai untuk database obat, perhitungan dosis, pemesanan obat, dan tatalaksana, sehingga dokter bisa berinteraksi langsung dengan AI lewat chat WhatsApp. Situs resminya ada di [doktergpt.id](https://doktergpt.id).

### Ringkasan

- **Nama produk:** DokterGPT
- **Website:** [doktergpt.id](https://doktergpt.id)
- **Kategori:** AI assistant untuk dokter
- **Fokus utama:** WhatsApp assistant, drug reference, dose calculation, ordering workflow, dan medical support
- **Peran:** Fullstack / AI integration engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan AI assistant untuk membantu aktivitas dokter sehari-hari.
- Memberikan akses ke database obat.
- Membantu menghitung dosis.
- Mendukung pemesanan obat melalui integrasi pihak ketiga.
- Membantu tatalaksana dan workflow kerja dokter.
- Berinteraksi langsung melalui **WhatsApp**.
- Memerlukan pembayaran melalui **Midtrans** untuk penggunaan layanan.

### Arsitektur dan Engineering

- Frontend website dibangun dengan:
  - **React**
- Backend dibangun dengan:
  - **Express**
- Model AI diintegrasikan dengan:
  - **LangChain**
  - **GPT-3.5**
- Terhubung dengan pihak ketiga untuk proses pemesanan obat.
- Menggunakan **WhatsApp** sebagai channel utama interaksi pengguna.

### Tantangan Teknis

- Merancang AI assistant agar relevan untuk kebutuhan dokter harian.
- Menghubungkan chat WhatsApp dengan alur AI secara mulus.
- Menjaga jawaban AI tetap berguna untuk konteks medis dan workflow dokter.
- Mengintegrasikan pemesanan obat dengan pihak ketiga.
- Menangani payment flow melalui Midtrans.
- Menjaga sistem tetap stabil untuk komunikasi chat yang bersifat real-time.

### Poin yang Bisa Ditambahkan Nanti

- Link demo atau screenshot alur WhatsApp assistant.
- Detail jenis pertanyaan yang didukung AI assistant.
- Detail integrasi pemesanan obat.
- Detail prompt, guardrail, atau alur LangChain.
- Detail payment flow dan subscription usage.
- Dampak produk, misalnya waktu yang dihemat dokter atau jumlah interaksi harian.
- Tanggung jawab spesifik di proyek: backend, frontend website, WhatsApp integration, AI workflow, ordering integration, atau payment integration.

## 8. ProcureX

**ProcureX** adalah super app pengadaan end-to-end untuk **Pupuk Indonesia**. Proyek ini berskala besar, memiliki banyak modul dan aplikasi di dalamnya, dan dibangun dengan arsitektur microservices. ProcureX juga terintegrasi dengan **SAP** untuk data karyawan atau user. Situs resminya ada di [procurement.pupuk-indonesia.com](https://procurement.pupuk-indonesia.com/).

### Ringkasan

- **Nama produk:** ProcureX
- **Website:** [procurement.pupuk-indonesia.com](https://procurement.pupuk-indonesia.com/)
- **Kategori:** End-to-end procurement super app
- **Fokus utama:** Procurement workflow, multi-module platform, microservices, dan enterprise integration
- **Client:** Pupuk Indonesia
- **Peran:** Fullstack / enterprise platform engineering
- **Status:** Portfolio project

### Fitur Utama

- Menjadi aplikasi pengadaan end-to-end untuk Pupuk Indonesia.
- Menggabungkan banyak modul dan sub-app dalam satu ekosistem produk.
- Mendukung workflow pengadaan berskala enterprise.
- Terintegrasi dengan SAP untuk data karyawan atau user.
- Menggunakan arsitektur microservices untuk memisahkan tanggung jawab sistem.

### Arsitektur dan Engineering

- Backend REST API dibangun dengan:
  - **Laravel Octane**
  - **Laravel**
- Arsitektur backend menggunakan:
  - **Microservices**
- Frontend dibangun dengan:
  - **React**
- Database menggunakan:
  - **PostgreSQL**
- Terintegrasi dengan:
  - **SAP**

### Tantangan Teknis

- Menjaga sistem enterprise besar tetap stabil dan terstruktur.
- Mengelola banyak modul dan aplikasi dalam satu super app.
- Menyesuaikan arsitektur microservices agar tiap domain tetap terpisah dengan jelas.
- Mengoptimalkan performa backend dengan Laravel Octane.
- Mengintegrasikan data user dan karyawan dari SAP.
- Menjaga konsistensi data antar service, modul, dan workflow procurement.

### Poin yang Bisa Ditambahkan Nanti

- Link dashboard atau screenshot modul utama ProcureX.
- Detail modul-modul yang ada di dalam super app.
- Detail alur procurement end-to-end.
- Detail integrasi SAP.
- Detail service boundaries pada arsitektur microservices.
- Volume user atau transaksi procurement yang ditangani.
- Dampak bisnis, misalnya efisiensi proses pengadaan atau waktu approval yang berkurang.
- Tanggung jawab spesifik di proyek: backend microservices, frontend React, SAP integration, performance tuning, atau system design.

## 9. PikPak

**PikPak** adalah marketplace dengan model bisnis yang menggabungkan satu lokasi pasar menjadi satu kali pengiriman, berbeda dari marketplace pada umumnya yang biasanya memecah pengiriman per toko. Produk ini sudah tidak aktif lagi, tetapi pernah menjadi salah satu proyek dengan integrasi logistik dan payment yang cukup kompleks. Selain versi web, aku juga membangun PWA/TWA untuk PikPak sampai deployment ke Play Store. Situs resminya dulu ada di `pickpack.id`, namun sekarang sudah tidak aktif.

### Ringkasan

- **Nama produk:** PikPak
- **Website:** `pickpack.id` (sudah tidak aktif)
- **Kategori:** Marketplace
- **Fokus utama:** Marketplace aggregation, one-location shipment model, logistics integration, dan payment processing
- **Peran:** Fullstack / platform engineering
- **Status:** Produk sudah dihentikan

### Fitur Utama

- Menjadi marketplace dengan model pengiriman satu lokasi pasar menjadi satu shipment.
- Menangani order marketplace dengan pola fulfillment yang berbeda dari marketplace biasa.
- Terhubung dengan payment gateway.
- Mendukung proses back office dan admin operations.
- Mendukung PWA/TWA yang dideploy sampai ke Play Store.

### Arsitektur dan Engineering

- Backend REST API dibangun dengan:
  - **Laravel**
- Frontend dibangun dengan:
  - **Vue**
  - **Nuxt.js**
- Admin / back office dibangun dengan:
  - **Angular**
- Database menggunakan:
  - **MySQL**
- Payment gateway menggunakan:
  - **Midtrans**
  - **Sendit**

### Tantangan Teknis

- Mengelola shipment per lokasi, bukan per toko seperti marketplace biasa.
- Mengintegrasikan shipment satu per satu tanpa aggregator.
- Menangani integrasi langsung dengan beberapa pihak ketiga seperti:
  - **JNE**
  - **SiCepat**
  - **SAP**
- Menjaga alur order, shipment, dan payment tetap sinkron.
- Mengintegrasikan dua payment gateway dengan peran berbeda.
- Menyesuaikan business flow marketplace yang tidak standar.

### Poin yang Bisa Ditambahkan Nanti

- Screenshot marketplace atau admin/back office.
- Detail alur order dari checkout sampai shipment.
- Detail integrasi JNE, SiCepat, dan SAP.
- Detail payment flow dengan Midtrans dan Sendit.
- Penjelasan lebih spesifik tentang model pengiriman satu lokasi pasar.
- Dampak bisnis atau skala operasional sebelum produk dihentikan.
- Tanggung jawab spesifik di proyek: backend API, frontend marketplace, admin back office, logistics integration, payment integration, atau system design.

## 10. CLS Ecommerce

**CLS Ecommerce** adalah SaaS e-commerce seperti Shopify versi lokal. Platform ini dibangun dengan arsitektur multi-tenant sehingga tiap merchant dapat memiliki environment, data, dan operasional yang terpisah di dalam satu sistem.

### Ringkasan

- **Nama produk:** CLS Ecommerce
- **Kategori:** SaaS e-commerce / local Shopify alternative
- **Fokus utama:** Multi-tenant commerce platform, merchant storefront, dan e-commerce operations
- **Peran:** Fullstack / SaaS platform engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan platform SaaS untuk e-commerce.
- Mengelola merchant dan toko dalam sistem multi-tenant.
- Mendukung kebutuhan operasional e-commerce lokal.
- Menjadi alternatif Shopify untuk use case lokal.

### Arsitektur dan Engineering

- Frontend dibangun dengan:
  - **Nuxt**
  - **Vue**
- Backend dibangun dengan:
  - **Laravel REST API**
- Database menggunakan:
  - **MySQL**
- Arsitektur sistem menggunakan:
  - **Multi-tenant**

### Tantangan Teknis

- Merancang sistem multi-tenant agar data antar merchant tetap terisolasi.
- Menjaga struktur aplikasi tetap fleksibel untuk banyak tenant.
- Mengelola konfigurasi dan konteks merchant di level platform.
- Menyeimbangkan kebutuhan SaaS umum dengan kebutuhan lokal merchant.

### Poin yang Bisa Ditambahkan Nanti

- Link dashboard atau screenshot storefront dan admin.
- Detail pendekatan multi-tenant yang dipakai.
- Detail alur merchant onboarding.
- Detail struktur data tenant, store, dan user.
- Dampak bisnis, misalnya jumlah merchant atau toko yang aktif.
- Tanggung jawab spesifik di proyek: backend multi-tenant, frontend Nuxt/Vue, admin panel, store management, atau system design.

## 11. BNI Klaster

**BNI Klaster** adalah static campaign website untuk divisi UMKM BNI. Website ini dibangun sebagai template website dengan HTML, CSS, dan JavaScript, dengan fokus utama pada implementasi UI manual yang mengikuti custom design dan kebutuhan klien.

### Ringkasan

- **Nama produk:** BNI Klaster
- **Kategori:** Static campaign website
- **Fokus utama:** Campaign website, custom UI implementation, dan frontend hand-coding
- **Client:** BNI Klaster divisi UMKM
- **Peran:** Frontend engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan website campaign statis.
- Dibangun sebagai template website sederhana.
- Menggunakan HTML, CSS, dan JavaScript.
- Mengikuti custom UI sesuai desain dan keinginan client.

### Arsitektur dan Engineering

- Dibangun dengan:
  - **HTML**
  - **CSS**
  - **JavaScript**
- Website bersifat statis.

### Tantangan Teknis

- Mengimplementasikan custom UI secara manual.
- Menyesuaikan hasil frontend dengan desain client secara presisi.
- Menjaga tampilan tetap rapi dan konsisten meskipun dibangun tanpa framework besar.
- Mengubah desain visual menjadi halaman website yang sesuai dengan kebutuhan campaign.

### Poin yang Bisa Ditambahkan Nanti

- Screenshot homepage atau section utama campaign.
- Detail layout dan komponen yang dibuat manual.
- Detail requirement visual dari client.
- Dampak campaign, misalnya traffic atau engagement.
- Tanggung jawab spesifik di proyek: layout implementation, responsive styling, UI matching, atau static frontend development.

## 12. Lokolaborasi by Kumparan

**Lokolaborasi by Kumparan** adalah static campaign website untuk event campaign dari Kumparan. Proyek ini punya challenge dan objektif yang sama seperti BNI Klaster, yaitu membangun website statis dengan HTML, CSS, dan JavaScript sambil mengikuti custom UI dan desain client secara manual.

### Ringkasan

- **Nama produk:** Lokolaborasi by Kumparan
- **Kategori:** Static campaign website
- **Fokus utama:** Event campaign website, custom UI implementation, dan frontend hand-coding
- **Client:** Kumparan
- **Peran:** Frontend engineering
- **Status:** Portfolio project

### Fitur Utama

- Menyediakan website campaign statis untuk event Kumparan.
- Dibangun sebagai template website sederhana.
- Menggunakan HTML, CSS, dan JavaScript.
- Mengikuti custom UI sesuai desain dan keinginan client.

### Arsitektur dan Engineering

- Dibangun dengan:
  - **HTML**
  - **CSS**
  - **JavaScript**
- Website bersifat statis.

### Tantangan Teknis

- Mengimplementasikan custom UI secara manual.
- Menyesuaikan hasil frontend dengan desain client secara presisi.
- Menjaga tampilan tetap rapi dan konsisten meskipun dibangun tanpa framework besar.
- Mengubah desain visual menjadi halaman website yang sesuai dengan kebutuhan campaign.

### Poin yang Bisa Ditambahkan Nanti

- Screenshot homepage atau section utama campaign.
- Detail layout dan komponen yang dibuat manual.
- Detail requirement visual dari client.
- Dampak campaign, misalnya traffic atau engagement.
- Tanggung jawab spesifik di proyek: layout implementation, responsive styling, UI matching, atau static frontend development.

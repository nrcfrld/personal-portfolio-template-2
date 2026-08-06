from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/pdf/enrico-feraldo-portfolio-id.pdf"
ASSET_DIR = ROOT / "assets"

W, H = A4
M = 18 * mm
CONTENT_W = W - (2 * M)

BLACK = colors.HexColor("#101014")
INK = colors.HexColor("#19191f")
MUTED = colors.HexColor("#5d6470")
LINE = colors.HexColor("#dedfe5")
GREEN = colors.HexColor("#15803d")
BLUE = colors.HexColor("#2563eb")
BG = colors.HexColor("#f7f7f4")


def draw_wrapped(c, text, x, y, max_w, size=8.2, leading=11, color=INK, font="Helvetica"):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line = ""
    for word in words:
        test = (line + " " + word).strip()
        if stringWidth(test, font, size) <= max_w:
            line = test
        else:
            c.drawString(x, y, line)
            y -= leading
            line = word
    if line:
        c.drawString(x, y, line)
        y -= leading
    return y


def header(c, title, category, link=None):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(M, H - M, title)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(M, H - M - 10, category)
    if link:
        label = f"Link: {link}"
        c.setFont("Helvetica-Bold", 8.2)
        badge_w = stringWidth(label, "Helvetica-Bold", 8.2) + 8 * mm
        badge_h = 7.5 * mm
        badge_x = W - M - badge_w
        badge_y = H - M - 13.5
        c.setStrokeColor(colors.HexColor("#b8cdfc"))
        c.setFillColor(colors.HexColor("#eef4ff"))
        c.roundRect(badge_x, badge_y, badge_w, badge_h, 2 * mm, stroke=1, fill=1)
        c.setFillColor(BLUE)
        c.drawCentredString(badge_x + badge_w / 2, badge_y + 2.4 * mm, label)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(M, H - M - 18, W - M, H - M - 18)
    return H - M - 28


def full_width_image(c, path, y):
    path = Path(path)
    if not path.exists():
        return y
    img = ImageReader(str(path))
    iw, ih = img.getSize()
    h = CONTENT_W * ih / iw
    c.drawImage(str(path), M, y - h, CONTENT_W, h, preserveAspectRatio=True, mask="auto")
    return y - h - 12


def two_cols(c, y, left_title, left_items, right_title, right_items):
    gap = 10 * mm
    cw = (CONTENT_W - gap) / 2

    def col(x, title, items):
        yy = y
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawString(x, yy, title.upper())
        yy -= 11
        for item in items:
            yy = draw_wrapped(c, "\u2022 " + item, x, yy, cw, 7.4, 9.2, INK)
        return yy

    return min(col(M, left_title, left_items), col(M + cw + gap, right_title, right_items))


def footer(c, page):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(M, 13 * mm, W - M, 13 * mm)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 5.8)
    c.drawString(M, 9 * mm, "Enrico Feraldo Kalengkongang - Dokumen Portfolio")
    c.drawRightString(W - M, 9 * mm, f"Halaman {page}")


def project_page(c, page, data):
    y = header(c, data["name"], data["category"], data.get("link"))
    if data.get("image"):
        y = full_width_image(c, ASSET_DIR / data["image"], y)
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(M, y, "RINGKASAN")
    y -= 10
    y = draw_wrapped(c, data["summary"], M, y, CONTENT_W, 8.3, 11, INK)
    y -= 8
    y = two_cols(c, y, "Kontribusi utama", data["role"], "Stack", data["stack"])
    y -= 8
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(M, y, "TANTANGAN / DAMPAK")
    y -= 10
    draw_wrapped(c, data["challenge"], M, y, CONTENT_W, 7.8, 10, INK)
    footer(c, page)
    c.showPage()


PROJECTS = [
    {
        "name": "Taroo",
        "category": "AI Landing Page Builder - Product Engineering",
        "link": "taroo.id",
        "image": "taroo-thumbnail.png",
        "summary": "Taroo adalah AI landing page builder untuk membuat halaman campaign, menerbitkan subdomain otomatis, dan memasang tracking Meta Pixel serta Google Analytics langsung dari produk.",
        "role": [
            "Membangun arsitektur monorepo dan alur deployment CI/CD.",
            "Mengembangkan frontend React/Vite/Astro dan backend NestJS.",
            "Mengintegrasikan subscription recurring payment dengan Xendit sebagai gateway utama dan Midtrans sebagai backup.",
        ],
        "stack": [
            "React, Vite, Astro, NestJS, PostgreSQL",
            "Monorepo, CI/CD, subdomain automation",
            "Meta Pixel, Google Analytics, Xendit, Midtrans",
        ],
        "challenge": "Kompleksitas utama ada pada pengelolaan lifecycle landing page, provisioning subdomain, tracking event, serta reliability recurring payment agar campaign bisa live cepat tanpa proses manual.",
    },
    {
        "name": "Colabo",
        "category": "AI Project Management - Platform Engineering",
        "link": "colabo.hecolab.id",
        "image": "colabo-thumbnail.webp",
        "summary": "Colabo adalah AI project management tools yang membantu project lead memahami kondisi proyek dari task, komentar, dan aktivitas yang tersebar.",
        "role": [
            "Merancang fitur AI summary untuk weekly report dan insight proyek.",
            "Membangun integrasi Telegram/WhatsApp assistant untuk percakapan dengan LLM.",
            "Membuat PDF report dan pipeline deployment otomatis ke VPS.",
        ],
        "stack": [
            "Go, Fiber, PostgreSQL",
            "React, Vite, Bun",
            "Gemini 3 Flash, Telegram/WhatsApp, GitHub Actions",
        ],
        "challenge": "Tantangan terbesarnya adalah mengambil konteks dari banyak task dan percakapan, lalu mengubahnya menjadi jawaban dan laporan yang ringkas dengan Gemini 3 Flash, relevan, dan bisa dikirim otomatis tiap minggu.",
    },
    {
        "name": "Gkomunika",
        "category": "Multivendor eSIM - Marketplace Ops Platform",
        "link": "gkomunika.com",
        "image": "gkomunika-thumbnail.webp",
        "summary": "Gkomunika adalah sistem agregasi order eSIM multivendor dari marketplace dan Shopify, lalu melakukan auto-fulfillment hingga QR Code dikirim ke customer.",
        "role": [
            "Mengintegrasikan webhook order dari Shopee, Tokopedia, TikTok Shop, dan Shopify.",
            "Membangun routing vendor berdasarkan SKU dan proses issue eSIM otomatis.",
            "Mengembangkan dashboard order internal dan pengiriman QR Code via email.",
        ],
        "stack": [
            "Express.js, Laravel, React, Vite",
            "Marketplace API, Shopify API, email delivery",
            "Multivendor eSIM integration",
        ],
        "challenge": "Sistem harus stabil karena bergantung pada banyak pihak ketiga. Setiap order perlu dipetakan ke vendor yang tepat, diproses otomatis, dan tetap punya fallback ketika API marketplace atau vendor berubah.",
    },
    {
        "name": "Sejawat IDN",
        "category": "LMS & Online Tryout - Medical Education",
        "link": "sejawatidn.com",
        "image": "sejawatidn-thumbnail.webp",
        "summary": "Sejawat IDN adalah platform LMS dan online tryout untuk bimbel kedokteran, termasuk penjualan materi, video pembelajaran, payment gateway, dan evaluasi ujian.",
        "role": [
            "Membangun backend API Laravel, user app Next.js/React, dan admin dashboard React/Vite.",
            "Menghandle tryout dengan 1.000-2.000 concurrent users.",
            "Mengimplementasikan scoring variatif, pembahasan soal, dan pembayaran Midtrans.",
        ],
        "stack": [
            "Laravel REST API, MySQL",
            "Next.js, React, Vite",
            "Midtrans, concurrent tryout workflow",
        ],
        "challenge": "Bagian paling kritikal adalah menjaga performa dan konsistensi data saat ribuan peserta mengerjakan tryout bersamaan, termasuk penyimpanan jawaban dan perhitungan skor akhir.",
    },
    {
        "name": "Hexchool",
        "category": "Coding LMS - Software Engineering Education",
        "link": "hexschool.com",
        "image": "hexchool-thumbnail.webp",
        "summary": "Hexchool adalah platform LMS untuk pembelajaran software engineering, bootcamp, private course, manajemen materi, pembayaran, dan sertifikat.",
        "role": [
            "Membangun frontend learner app dengan Next.js dan admin dashboard React/Vite.",
            "Menyediakan REST API Laravel untuk course, bootcamp, certificate, dan payment workflow.",
            "Menyiapkan Docker untuk kebutuhan CI/CD.",
        ],
        "stack": [
            "Next.js, React, Vite",
            "Laravel REST API",
            "Docker, payment gateway, certificate module",
        ],
        "challenge": "Platform membutuhkan alur belajar yang rapi dari pembelian, akses materi, kelas, sampai sertifikat, dengan pemisahan aplikasi end-user dan admin agar operasional konten tetap mudah dikelola.",
    },
    {
        "name": "Kelas Drafter",
        "category": "Architecture LMS - Online Course Platform",
        "link": "kelasdrafter.id",
        "image": "kelasdrafter-thumbnail.webp",
        "summary": "Kelas Drafter adalah LMS untuk bootcamp dan online course bidang arsitektur, termasuk video course, materi, pembayaran, dan dashboard admin.",
        "role": [
            "Membangun backend Laravel REST API dan database MySQL.",
            "Mengembangkan frontend Next.js untuk user dan React untuk admin/owner dashboard.",
            "Mengintegrasikan payment gateway Midtrans untuk pembelian course.",
        ],
        "stack": [
            "Laravel REST API, MySQL",
            "Next.js, React",
            "Midtrans, course management",
        ],
        "challenge": "Fokus utamanya adalah membuat pengalaman pembelian dan akses course yang stabil, sederhana, dan mudah dikelola oleh owner tanpa proses manual yang berulang.",
    },
    {
        "name": "DokterGPT",
        "category": "AI Assistant - Healthcare Workflow",
        "link": "doktergpt.id",
        "image": "doktergpt-thumbnail.webp",
        "summary": "DokterGPT adalah AI assistant via WhatsApp untuk membantu dokter dalam aktivitas harian seperti informasi obat, kalkulasi dosis, pemesanan obat, dan tata laksana.",
        "role": [
            "Membangun backend Express dan website React.",
            "Mengintegrasikan LangChain dengan GPT-3.5 serta WhatsApp sebagai channel utama.",
            "Menghubungkan payment Midtrans dan integrasi pihak ketiga untuk pemesanan obat.",
        ],
        "stack": [
            "Express, React",
            "LangChain, GPT-3.5, WhatsApp integration",
            "Midtrans, third-party medicine ordering",
        ],
        "challenge": "Produk ini menuntut desain alur AI yang praktis untuk konteks medis sehari-hari, dengan akses melalui WhatsApp agar dokter bisa bertanya tanpa membuka aplikasi tambahan.",
    },
    {
        "name": "ProcureX",
        "category": "Enterprise Procurement Super App",
        "link": "procurement.pupuk-indonesia.com",
        "image": "procurex-thumbnail.jpg",
        "summary": "ProcureX adalah super app end-to-end procurement untuk Pupuk Indonesia, mencakup banyak modul pengadaan dalam arsitektur microservices.",
        "role": [
            "Membangun REST API berbasis Laravel Octane dalam pendekatan microservices.",
            "Mengembangkan frontend React untuk modul-modul procurement.",
            "Mengintegrasikan sistem dengan SAP untuk data user/karyawan.",
        ],
        "stack": [
            "Laravel Octane, PostgreSQL",
            "React",
            "Microservices, SAP integration",
        ],
        "challenge": "Skalanya enterprise: banyak modul, integrasi SAP, kebutuhan reliability tinggi, dan pemisahan service agar proses procurement dapat berjalan end-to-end secara konsisten.",
    },
    {
        "name": "PikPak",
        "category": "Marketplace - Discontinued Product",
        "link": "youtube.com/watch?v=OsnVKkVqSBs",
        "summary": "PikPak adalah marketplace dengan model satu lokasi pasar sebagai satu pengiriman, berbeda dari marketplace umum yang biasanya menghitung pengiriman per toko.",
        "role": [
            "Membangun backend Laravel REST API, frontend Vue/Nuxt, dan Angular back office.",
            "Mengintegrasikan shipment langsung ke JNE dan SiCepat tanpa aggregator.",
            "Membangun PWA/TWA dan deployment sampai Play Store.",
        ],
        "stack": [
            "Laravel REST API, MySQL",
            "Vue, Nuxt.js, Angular",
            "JNE, SiCepat, SAP, Midtrans, Xendit",
        ],
        "challenge": "Tantangan terbesar ada pada model fulfillment dan shipment non-standar, integrasi logistik satu per satu, serta payment gateway ganda untuk mendukung transaksi marketplace.",
    },
    {
        "name": "CLS Ecommerce",
        "category": "SaaS Ecommerce",
        "summary": "CLS Ecommerce adalah SaaS ecommerce lokal seperti Shopify versi sederhana, ditujukan agar merchant bisa memiliki toko online sendiri.",
        "role": [
            "Membangun arsitektur multitenant untuk toko dan merchant.",
            "Mengembangkan backend Laravel REST API dan frontend Nuxt/Vue.",
            "Menyiapkan struktur data toko, produk, dan tenant isolation.",
        ],
        "stack": [
            "Nuxt.js, Vue",
            "Laravel REST API, MySQL",
            "Multitenant architecture",
        ],
        "challenge": "Bagian paling penting adalah desain multitenancy: pemisahan data antar merchant, routing tenant, dan fondasi agar satu codebase dapat melayani banyak toko.",
    },
    {
        "name": "BNI Klaster",
        "category": "Static Campaign Website",
        "image": "bni-klaster-thumbnail.webp",
        "summary": "BNI Klaster adalah template website statis untuk campaign divisi UMKM BNI.",
        "role": [
            "Mengimplementasikan halaman dari custom UI design secara manual.",
            "Membangun HTML/CSS/JavaScript tanpa framework.",
            "Menyesuaikan detail visual sesuai arahan client.",
        ],
        "stack": ["HTML, CSS, JavaScript", "Static website", "Custom UI implementation"],
        "challenge": "Walaupun sederhana secara teknis, tantangannya ada pada presisi implementasi visual dan penyesuaian manual agar hasil akhir mengikuti desain serta ekspektasi client.",
    },
    {
        "name": "Lokolaborasi by Kumparan",
        "category": "Static Campaign Website",
        "summary": "Lokolaborasi by Kumparan adalah website campaign event Kumparan untuk kebutuhan publikasi dan komunikasi event.",
        "role": [
            "Mengimplementasikan static campaign page sesuai kebutuhan event.",
            "Menerjemahkan desain menjadi HTML/CSS/JavaScript yang ringan.",
            "Menjaga tampilan tetap konsisten dan responsif.",
        ],
        "stack": ["HTML, CSS, JavaScript", "Static website", "Manual responsive implementation"],
        "challenge": "Fokusnya adalah eksekusi cepat dan presisi untuk campaign/event, dengan tampilan yang sesuai brand dan tetap ringan untuk akses publik.",
    },
]


def cover(c):
    c.setFillColor(BLACK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 9)
    c.drawString(M, H - 48 * mm, "Dokumen Portfolio")
    c.setFont("Helvetica-Bold", 27)
    c.drawString(M, H - 65 * mm, "Enrico Feraldo")
    c.drawString(M, H - 79 * mm, "Kalengkongang")
    c.setFillColor(colors.HexColor("#c9cbd1"))
    c.setFont("Helvetica", 10)
    c.drawString(M, H - 94 * mm, "Fullstack Engineer")
    c.setStrokeColor(colors.HexColor("#555762"))
    c.setLineWidth(0.7)
    c.line(M, H - 107 * mm, W - M, H - 107 * mm)
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor("#f3f3f5"))
    contacts = ["Laravel, React, Go, Node.js", "AI products, LMS, marketplace, SaaS", "+62 8953 2137 9775"]
    y = H - 123 * mm
    for item in contacts:
        c.drawString(M, y, item)
        y -= 10 * mm
    footer(c, 1)
    c.showPage()


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4)
    c.setTitle("Dokumen Portfolio - Enrico Feraldo Kalengkongang")
    cover(c)
    for idx, project in enumerate(PROJECTS, 2):
        project_page(c, idx, project)
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()

const toastTriggers = document.querySelectorAll("[data-toast-trigger]");
const navToggle = document.querySelector("[data-nav-toggle]");
const instagramSlider = document.querySelector("[data-instagram-slider]");
const instagramPrev = document.querySelector("[data-instagram-prev]");
const instagramNext = document.querySelector("[data-instagram-next]");
const portfolioPreviewTriggers = document.querySelectorAll("[data-portfolio-preview]");
const portfolioModal = document.querySelector("[data-portfolio-modal]");
const portfolioModalImage = document.querySelector("[data-portfolio-modal-image]");
const portfolioModalCloseTriggers = document.querySelectorAll("[data-portfolio-modal-close]");
let portfolioModalReturnTarget = null;

if (navToggle) {
  const siteHeader = navToggle.closest(".site-header");
  const nav = document.getElementById(navToggle.getAttribute("aria-controls"));

  const setNavOpen = (isOpen) => {
    siteHeader?.classList.toggle("is-nav-open", isOpen);
    navToggle.setAttribute("aria-expanded", String(isOpen));
  };

  navToggle.addEventListener("click", () => {
    const isOpen = navToggle.getAttribute("aria-expanded") === "true";
    setNavOpen(!isOpen);
  });

  nav?.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      setNavOpen(false);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setNavOpen(false);
    }
  });
}

toastTriggers.forEach((trigger) => {
  trigger.addEventListener("click", () => {
    const panel = trigger.closest(".panel");
    const message = panel?.querySelector("[data-toast-message]");

    if (message) {
      message.hidden = false;
    }

    trigger.textContent = "State Triggered";
  });
});

if (instagramSlider && instagramPrev && instagramNext) {
  const getSlideDistance = () => {
    const firstSlide = instagramSlider.querySelector(".instagram-post");
    const gap = Number.parseFloat(getComputedStyle(instagramSlider).columnGap) || 0;
    return firstSlide ? firstSlide.getBoundingClientRect().width + gap : instagramSlider.clientWidth;
  };

  const scrollSlider = (direction) => {
    instagramSlider.scrollBy({
      left: direction * getSlideDistance(),
      behavior: "smooth",
    });
  };

  instagramPrev.addEventListener("click", () => scrollSlider(-1));
  instagramNext.addEventListener("click", () => scrollSlider(1));
}

if (portfolioModal && portfolioModalImage) {
  const closeButton = portfolioModal.querySelector(".portfolio-preview-close");

  const closePortfolioModal = () => {
    portfolioModal.hidden = true;
    document.body.classList.remove("is-modal-open");
    portfolioModalImage.removeAttribute("src");
    portfolioModalImage.alt = "";
    portfolioModalReturnTarget?.focus();
    portfolioModalReturnTarget = null;
  };

  const openPortfolioModal = (trigger) => {
    const image = trigger.querySelector("img");

    if (!image) {
      return;
    }

    portfolioModalReturnTarget = trigger;
    portfolioModalImage.src = image.currentSrc || image.src;
    portfolioModalImage.alt = image.alt;
    portfolioModal.hidden = false;
    document.body.classList.add("is-modal-open");
    closeButton?.focus();
  };

  portfolioPreviewTriggers.forEach((trigger) => {
    trigger.addEventListener("click", () => openPortfolioModal(trigger));
  });

  portfolioModalCloseTriggers.forEach((trigger) => {
    trigger.addEventListener("click", closePortfolioModal);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !portfolioModal.hidden) {
      closePortfolioModal();
    }

    if (event.key === "Tab" && !portfolioModal.hidden && closeButton) {
      event.preventDefault();
      closeButton.focus();
    }
  });
}

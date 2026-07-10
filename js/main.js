document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".fb-nav-toggle");
  const nav = document.querySelector(".fb-header-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", nav.classList.contains("open"));
    });
  }
});

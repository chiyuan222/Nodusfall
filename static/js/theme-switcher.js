(function () {
  var switcher = document.getElementById("theme-switcher");
  if (!switcher || !window.THEME_PRESETS) return;

  var STORAGE_KEY = "ysxw-visitor-theme";
  var toggle = switcher.querySelector(".theme-toggle");
  var menu = switcher.querySelector(".theme-menu");
  var options = switcher.querySelectorAll(".theme-option");

  function applyTheme(key) {
    var preset = key && window.THEME_PRESETS[key] ? window.THEME_PRESETS[key] : null;
    var root = document.documentElement;
    ["accent_color", "panel_color", "text_color", "muted_color", "border_color"].forEach(function (name) {
      if (preset) {
        root.style.setProperty("--" + name.replace("_color", ""), preset.colors[name]);
      } else {
        root.style.removeProperty("--" + name.replace("_color", ""));
      }
    });
    if (preset) {
      localStorage.setItem(STORAGE_KEY, key);
    } else {
      localStorage.removeItem(STORAGE_KEY);
    }
    options.forEach(function (opt) {
      opt.classList.toggle("active", opt.getAttribute("data-theme") === key);
    });
  }

  toggle.addEventListener("click", function () {
    var opening = menu.hasAttribute("hidden");
    menu.toggleAttribute("hidden");
    toggle.classList.toggle("open", opening);
  });

  document.addEventListener("click", function (event) {
    if (!switcher.contains(event.target)) {
      menu.setAttribute("hidden", "");
      toggle.classList.remove("open");
    }
  });

  options.forEach(function (opt) {
    opt.addEventListener("click", function () {
      applyTheme(opt.getAttribute("data-theme"));
      menu.setAttribute("hidden", "");
      toggle.classList.remove("open");
    });
  });

  applyTheme(localStorage.getItem(STORAGE_KEY) || "");
})();

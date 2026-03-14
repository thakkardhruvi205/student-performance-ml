particlesJS("particles-js", {
  particles: {
    number: { value: 120 },

    color: { value: "#ffffff" },

    shape: { type: "circle" },

    opacity: {
      value: 0.5,
      random: true
    },

    size: {
      value: 3,
      random: true
    },

    line_linked: {
      enable: true,
      distance: 150,
      color: "#6366f1",
      opacity: 0.4,
      width: 1
    },

    move: {
      enable: true,
      speed: 2,
      direction: "none",
      random: false,
      straight: false
    }
  },

  interactivity: {
    detect_on: "canvas",

    events: {
      onhover: {
        enable: true,
        mode: "grab"
      }
    }
  }
});
const canvas = document.getElementById("bg");

const renderer = new THREE.WebGLRenderer({
  canvas: canvas,
});

renderer.setSize(window.innerWidth, window.innerHeight);

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

camera.position.z = 5;

const geometry = new THREE.BufferGeometry();
const vertices = [];

for (let i = 0; i < 5000; i++) {

  vertices.push(
    (Math.random() - 0.5) * 10,
    (Math.random() - 0.5) * 10,
    (Math.random() - 0.5) * 10
  );

}

geometry.setAttribute(
  "position",
  new THREE.Float32BufferAttribute(vertices, 3)
);

const material = new THREE.PointsMaterial({
  color: 0x6366f1,
  size: 0.02,
});

const stars = new THREE.Points(geometry, material);

scene.add(stars);

function animate() {

  requestAnimationFrame(animate);

  stars.rotation.y += 0.0005;

  renderer.render(scene, camera);

}

animate();
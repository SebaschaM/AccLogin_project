const modal = document.querySelector(".modal");
const formLogin = document.getElementById("form");

formLogin.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(formLogin);
  const data = Object.fromEntries(formData);

  login(data);
});

async function login(data) {
  const response = await fetch("/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const responseJson = await response.json();

  if (responseJson.hasError) {
    modal.classList.remove("hidden");
    const modalTitle = document.querySelector(".modal__title");
    modalTitle.textContent = "Error";
    const modalText = document.querySelector(".modal__text");
    modalText.textContent = responseJson.message;

    const modalBtn = document.querySelector(".modal__btn");
    modalBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
  } else {
    modal.classList.remove("hidden");
    const modalTitle = document.querySelector(".modal__title");
    modalTitle.textContent = "Success";

    const modalText = document.querySelector(".modal__text");
    modalText.textContent = responseJson.message;

    const modalBtn = document.querySelector(".modal__btn");
    modalBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
  }
}


  const nav = document.querySelector(".nav-menu");
  const navBtn = document.querySelector("#navBtn")
  const overLay = document.querySelector(".overlay")

  navBtn.addEventListener("click", () => {
     nav.classList.add('open');
     overLay.classList.add('open');
  });

  overLay.addEventListener("click", () =>{
     nav.classList.remove('open');
     overLay.classList.remove('open');
  });

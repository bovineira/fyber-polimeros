// ============================================
// FYBER POLÍMEROS - SCRIPTS
// ============================================

// Header scroll effect
document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('header');
  
  if (header) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
  
  // Menu mobile toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('nav');
  
  if (menuToggle && nav) {
    menuToggle.addEventListener('click', function() {
      nav.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      if (!nav.contains(e.target) && !menuToggle.contains(e.target)) {
        nav.classList.remove('active');
      }
    });
  }
  
  // Active menu item
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('nav a');
  
  navLinks.forEach(link => {
    const linkPage = link.getAttribute('href');
    if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
      link.classList.add('active');
    }
  });
  
  // Dropdown menu
  const dropdowns = document.querySelectorAll('.dropdown');
  
  dropdowns.forEach(dropdown => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    
    if (toggle) {
      // Toggle on click
      toggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        // Close other dropdowns
        dropdowns.forEach(d => {
          if (d !== dropdown) {
            d.classList.remove('active');
          }
        });
        
        dropdown.classList.toggle('active');
      });
      
      // Close on outside click
      document.addEventListener('click', function(e) {
        if (!dropdown.contains(e.target)) {
          dropdown.classList.remove('active');
        }
      });
      
      // Hover for desktop
      if (window.innerWidth > 768) {
        dropdown.addEventListener('mouseenter', function() {
          dropdown.classList.add('active');
        });
        
        dropdown.addEventListener('mouseleave', function() {
          dropdown.classList.remove('active');
        });
      }
    }
  });
});

// ============================================
// HERO SLIDESHOW
// ============================================

function initSlideshow() {
  const slides = document.querySelectorAll('.slide');
  const bullets = document.querySelectorAll('.slide-bullet');
  const prevBtn = document.querySelector('.slide-arrow.prev');
  const nextBtn = document.querySelector('.slide-arrow.next');
  
  if (slides.length === 0) return;
  
  let currentSlide = 0;
  let slideInterval;
  
  function showSlide(index) {
    // Remove active de todos primeiro
    slides.forEach((slide, i) => {
      slide.classList.remove('active');
      if (bullets[i]) {
        bullets[i].classList.remove('active');
      }
    });
    
    // Pequeno delay para garantir a animação suave
    setTimeout(() => {
      slides[index].classList.add('active');
      if (bullets[index]) {
        bullets[index].classList.add('active');
      }
    }, 50);
    
    currentSlide = index;
  }
  
  function nextSlide() {
    const next = (currentSlide + 1) % slides.length;
    showSlide(next);
  }
  
  function prevSlide() {
    const prev = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(prev);
  }
  
  function startSlideshow() {
    slideInterval = setInterval(nextSlide, 6500);
  }
  
  function stopSlideshow() {
    clearInterval(slideInterval);
  }
  
  // Event listeners
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      nextSlide();
      stopSlideshow();
      startSlideshow();
    });
  }
  
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      prevSlide();
      stopSlideshow();
      startSlideshow();
    });
  }
  
  bullets.forEach((bullet, index) => {
    bullet.addEventListener('click', () => {
      showSlide(index);
      stopSlideshow();
      startSlideshow();
    });
  });
  
  // Pause on hover
  const slideshow = document.querySelector('.hero-slideshow');
  if (slideshow) {
    slideshow.addEventListener('mouseenter', stopSlideshow);
    slideshow.addEventListener('mouseleave', startSlideshow);
  }
  
  // Start slideshow
  showSlide(0);
  startSlideshow();
}

// ============================================
// CARROSSEL DE BENEFÍCIOS (Auto-scroll)
// ============================================

function initBeneficiosCarousel() {
  const carousel = document.querySelector('.beneficios-carousel');
  if (!carousel) return;
  
  // Duplicar cards para loop infinito
  const cards = carousel.querySelectorAll('.beneficio-card');
  if (cards.length > 0) {
    cards.forEach(card => {
      const clone = card.cloneNode(true);
      carousel.appendChild(clone);
    });
  }
}

// ============================================
// CARROSSEL MAIS VENDIDOS
// ============================================

function initProdutosCarousel() {
  const wrappers = document.querySelectorAll('.produtos-wrapper');
  
  wrappers.forEach(wrapper => {
    const carousel = wrapper.closest('.produtos-carousel');
    const prevBtn = carousel ? carousel.querySelector('.carousel-btn.prev') : null;
    const nextBtn = carousel ? carousel.querySelector('.carousel-btn.next') : null;
    
    initSingleCarousel(wrapper, prevBtn, nextBtn);
  });
}

function initSingleCarousel(wrapper, prevBtn, nextBtn) {
  if (!wrapper) return;
  
  const cards = wrapper.querySelectorAll('.produto-card');
  if (cards.length === 0) return;
  
  let currentIndex = 0;
  const cardsPerView = getCardsPerView();
  
  function getCardsPerView() {
    if (window.innerWidth <= 768) return 1;
    if (window.innerWidth <= 1024) return 2;
    return 3;
  }
  
  function updateCarousel() {
    const cardWidth = cards[0].offsetWidth;
    const gap = 32; // 2rem
    const scrollAmount = (cardWidth + gap) * currentIndex;
    
    wrapper.scrollTo({
      left: scrollAmount,
      behavior: 'smooth'
    });
    
    updateButtons();
  }
  
  function updateButtons() {
    const maxIndex = Math.max(0, cards.length - getCardsPerView());
    
    if (prevBtn) {
      prevBtn.disabled = currentIndex === 0;
    }
    
    if (nextBtn) {
      nextBtn.disabled = currentIndex >= maxIndex;
    }
  }
  
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const maxIndex = Math.max(0, cards.length - getCardsPerView());
      if (currentIndex < maxIndex) {
        currentIndex++;
        updateCarousel();
      }
    });
  }
  
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
      }
    });
  }
  
  // Update on resize
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      currentIndex = 0;
      updateCarousel();
    }, 250);
  });
  
  updateButtons();
}

// ============================================
// SCROLL ANIMATIONS
// ============================================

function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  // Observe all fade-in elements
  document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el);
  });
}

// ============================================
// FORMULÁRIO DE CONTATO
// ============================================

function initContactForm() {
  const forms = document.querySelectorAll('.contato-form');
  
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const formData = new FormData(form);
      const nome = formData.get('nome') || form.querySelector('[name="nome"]')?.value;
      const email = formData.get('email') || form.querySelector('[name="email"]')?.value;
      const produto = formData.get('produto') || form.querySelector('[name="produto"]')?.value;
      
      // Criar mailto link
      const subject = encodeURIComponent('Contato - Fyber Polímeros');
      const body = encodeURIComponent(
        `Olá, meu nome é ${nome}.\n\n` +
        `E-mail: ${email}\n\n` +
        `Produto/Serviço de interesse: ${produto}\n\n` +
        `Gostaria de receber mais informações.`
      );
      
      const mailtoLink = `mailto:contato@fyberpolimeros.com.br?subject=${subject}&body=${body}`;
      
      // Abrir cliente de e-mail
      window.location.href = mailtoLink;
      
      // Mostrar mensagem de sucesso
      const successMsg = document.createElement('div');
      successMsg.textContent = 'Formulário enviado! Seu cliente de e-mail será aberto.';
      successMsg.style.cssText = 'background: #10B981; color: white; padding: 1rem; border-radius: 8px; margin-top: 1rem; text-align: center;';
      form.appendChild(successMsg);
      
      setTimeout(() => {
        successMsg.remove();
      }, 5000);
    });
  });
}

// ============================================
// CARREGAR PRODUTOS DO JSON
// ============================================

async function loadProdutos() {
  try {
    const response = await fetch('data/produtos.json');
    const produtos = await response.json();
    return produtos;
  } catch (error) {
    console.error('Erro ao carregar produtos:', error);
    return [];
  }
}

function renderProdutoCard(produto, isCarousel = false) {
  const cardClass = isCarousel ? 'produto-card' : 'produto-grid-card';
  const imageClass = isCarousel ? 'produto-card-image' : 'produto-grid-card-image';
  const contentClass = isCarousel ? 'produto-card-content' : 'produto-grid-card-content';
  
  return `
    <div class="${cardClass} fade-in">
      <img src="${produto.imagem}" alt="${produto.nome}" class="${imageClass}" loading="lazy">
      <div class="${contentClass}">
        <h3>${produto.nome}</h3>
        <p>${produto.descricao}</p>
        ${!isCarousel ? `
          <div class="produto-grid-card-actions">
            <a href="https://wa.me/5500000000000?text=Olá,%20quero%20falar%20com%20um%20consultor%20da%20Fyber%20Polímeros%20sobre%20${encodeURIComponent(produto.nome)}" 
               class="btn btn-primary btn-whatsapp" target="_blank" rel="noopener">
              Falar no WhatsApp
            </a>
            <a href="produto-${produto.slug}.html" class="btn btn-secondary">Ver detalhes</a>
          </div>
        ` : `
          <a href="https://wa.me/5500000000000?text=Olá,%20quero%20falar%20com%20um%20consultor%20da%20Fyber%20Polímeros%20sobre%20${encodeURIComponent(produto.nome)}" 
             class="btn btn-primary btn-whatsapp" target="_blank" rel="noopener">
            Falar no WhatsApp
          </a>
          <a href="produto-${produto.slug}.html" class="btn btn-secondary" style="margin-top: 0.5rem;">Ver detalhes</a>
        `}
      </div>
    </div>
  `;
}

// ============================================
// BOTÃO EXIBIR MAIS
// ============================================

function initExibirMais() {
  const buttons = document.querySelectorAll('.exibir-mais-btn');
  
  buttons.forEach(button => {
    button.addEventListener('click', function() {
      const carouselId = this.getAttribute('data-carousel');
      const wrapper = this.closest('.produtos-carousel').querySelector('.produtos-wrapper');
      const hiddenItems = wrapper.querySelectorAll('.produto-item[data-visible="false"]');
      
      // Mostrar todos os produtos ocultos
      hiddenItems.forEach(item => {
        item.setAttribute('data-visible', 'true');
        item.style.display = 'flex';
        item.classList.add('fade-in');
      });
      
      // Esconder o botão após exibir todos
      if (hiddenItems.length > 0) {
        this.style.display = 'none';
      }
      
      // Re-inicializar animações
      setTimeout(() => {
        initScrollAnimations();
      }, 100);
    });
  });
}

// ============================================
// INICIALIZAÇÃO
// ============================================

document.addEventListener('DOMContentLoaded', function() {
  initSlideshow();
  initBeneficiosCarousel();
  initProdutosCarousel();
  initScrollAnimations();
  initContactForm();
  initExibirMais();
  
  // NÃO substituir produtos - eles já estão hardcoded no HTML
  // Apenas inicializar animações para os produtos existentes
  const produtosGrid = document.querySelector('.produtos-grid');
  
  if (produtosGrid) {
    // Re-inicializar animações para os elementos existentes
    setTimeout(() => {
      initScrollAnimations();
    }, 100);
  }
  
  // Inicializar carrosséis que já têm conteúdo (Mais Vendidos e Destaques)
  const produtosCarousel = document.querySelectorAll('.produtos-wrapper');
  if (produtosCarousel.length > 0) {
    produtosCarousel.forEach(wrapper => {
      // Se o wrapper já tem conteúdo (placeholders), apenas inicializar o carrossel
      if (wrapper.children.length > 0) {
        setTimeout(() => {
          initProdutosCarousel();
          initScrollAnimations();
        }, 100);
      }
    });
  }
});



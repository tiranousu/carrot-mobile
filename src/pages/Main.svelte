<script>
  let hour = new Date().getHours();
  let min = new Date().getMinutes();
</script>

<div class="media-info-msg">화면사이즈를 줄여줘</div>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/char-bar.svg" alt="" />
      <img src="assets/wifi.svg" alt="" />
      <img src="assets/battery.svg" alt="" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div>역삼1동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow-down.svg" alt=""/>
      </div>
    </div>
    <div class="menu-bar__icons">
      <img src="assets/search.svg" alt="" /> 
      <img src="assets/menu.svg" alt="" />
      <img src="assets/alert.svg" alt="" />
    </div>
  </div>
</header>
<main>
    
  <a class="write-btn" href="#/write">+글쓰기</a>
      
      </main>
  
      <div>
        
      </div>
  
      <footer>
        <div class="footer-block">
          <div class="footer-icons">
            <div class="footer-icons__img">
              <img src="assets/home.svg" alt=""/>
            </div>
            <div class="footer-icons__desc">홈</div>
          </div>
          <div class="footer-icons">
            <div class="footer-icons__img">
              <img src="assets/doc.svg" alt="" />
            </div>
            <div class="footer-icons__desc">동네생활</div>
          </div>
          <div class="footer-icons">
            <div class="footer-icons__img">
              <img src="assets/location.svg" alt=""/>
            </div>
            <div class="footer-icons__desc">내근처</div>
          </div>
          <div class="footer-icons">
            <div class="footer-icons__img">
              <img src="assets/chat.svg" alt=""/>
            </div>
            <div class="footer-icons__desc">채팅</div>
          </div>
          <div class="footer-icons">
            <div class="footer-icons__img">
              <img src="assets/user.svg" alt="" />
            </div>
            <div class="footer-icons__desc">나의당근</div>
          </div>
        </div>
      </footer>

    <style>
      .info-bar__time{
        color:blue
      }
    </style>
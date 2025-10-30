<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AESPA – Rich Man</title>
    
  <style>
    /* Mengimpor font */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;500;700&display=swap');

    /* Mengubah .body menjadi body (selector tag) */
    body {
      margin: 0;
      font-family: "Poppins", sans-serif;
      /* Hapus background-color lama */
      color: white;
      display: flex; /* Menggunakan flex untuk layout 2 kolom */
      height: 100vh;
      overflow: hidden;
      
      /* --- KODE GRADIENT MENYATU BARU --- */
      background: linear-gradient(to bottom, 
                  #007bff 0%,     /* Biru terang (mulai atas) */
                  #dc3545 35%,    /* Transisi ke Merah */
                  #28a745 65%,    /* Transisi ke Hijau */
                  #ffc107 100%);  /* Kuning (sampai bawah) */
      /* ---------------------------------- */
    }

    /* Bagian kiri (LIRIK) - sebelumnya .right-section */
    .left-lyrics-section {
      width: 65%;
      padding: 40px;
      box-sizing: border-box;
      overflow-y: auto; /* Lirik bisa di-scroll */
    }

    /* Bagian kanan (SIDEBAR) - BARU */
    .right-sidebar-section {
      width: 35%;
      height: 100vh; /* Tinggi penuh */
      overflow-y: auto; /* Sidebar bisa di-scroll jika konten panjang */
      box-sizing: border-box;
      padding: 20px;
      display: flex;
      flex-direction: column; /* Menumpuk producer box di atas foto */
    }

    /* Foto-foto - sebelumnya .left-section */
    .photo-grid {
      width: 100%; /* Lebar penuh mengisi sidebar */
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(3, 1fr);
      gap: 10px;
      box-sizing: border-box;
      align-content: center;
      justify-content: center;
    }

    .photo-grid img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 10px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }

    /* Judul Lirik */
    h1 {
      text-align: center;
      font-size: 2.8em;
      font-weight: 800;
      color: #fff;
      margin-bottom: 10px;
    }

    hr {
      width: 80px;
      border: 2px solid #ff477e;
      margin: 10px auto 30px auto;
    }

    h3 {
      color: #ff90b3;
      margin-top: 30px;
    }

    p {
      line-height: 1.7;
      font-size: 1em;
    }

    /* Kotak Produser & Songwriter */
    .producer-box {
      /* Menghapus position: absolute */
      background-color: rgba(255, 255, 255, 0.15);
      padding: 15px 20px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
      font-size: 0.9em;
      margin-bottom: 20px; /* Memberi jarak ke foto di bawahnya */
    }

    .producer-box h4 {
      margin: 0 0 8px 0;
      color: #ffb6c1;
    }

    .producer-box p {
      margin: 3px 0;
    }

    /* Scroll bar halus (berlaku global) */
    ::-webkit-scrollbar {
      width: 6px;
    }

    ::-webkit-scrollbar-thumb {
      background: #ff477e;
      border-radius: 4px;
    }

    /* Efek hover kecil */
    .photo-grid img:hover {
      transform: scale(1.03);
      transition: 0.3s ease-in-out;
    }
  </style>
</head>
<body>

  <div class="left-lyrics-section">
    <h1 class="lyric-title">AESPA – Rich Man</h1>
    <hr>

    <div class="lyric-box">
      <p class="lyric-section">[Intro: Giselle, Winter]</p>
      <p>My mom said to me<br>
      "Find someone who can give you everything"<br>
      And I said, "Mom, I already have everything"<br>
      I am a rich man, I am a rich man (I am a rich man)</p>

      <p class="lyric-section">[Chorus: Winter, Ningning]</p>
      <p>(I'ma carry myself) I am a rich man<br>
      (I'ma carry myself) I am a rich man<br>
      I'm my own biggest fan, and I'm high in demand<br>
      I am a rich man</p>

      <p class="lyric-section">[Verse 1: Karina, Giselle, Winter]</p>
      <p>Don't care about what they say<br>
      날 밀어 넣고 멋대로 굴 때<br>
      내 것을 탐내 see? My name is<br>
      Where my name is? (I am a rich man)<br>
      That's me, 나는 reckless (Yeah)<br>
      굳은 mental 그것쯤 웃네 (What?)<br>
      내가 날 이끌어 가, 보여 다음 sign<br>
      별거 아냐, exit is my next step</p>

      <p class="lyric-section">[Pre-Chorus: Ningning, Giselle, Winter, Karina]</p>
      <p>딴 생각 말고 self-belief<br>
      'Cause 그게 훨씬 재미있지<br>
      Ooh-woah, oh<br>
      I am a rich man<br>
      So I am standin', where you lookin'?<br>
      맞춘 듯한 my perfect fit<br>
      Baby (Hey, hey)<br>
      I am a rich man</p>

      <p class="lyric-section">[Chorus: Karina, Giselle, Ningning, Winter]</p>
      <p>(I'ma carry myself) I am a rich man<br>
      (I'ma carry myself) I am a rich man<br>
      I'm that one, 난 나로 가득해 by myself<br>
      I am a rich man<br>
      (I'ma carry myself) I am a rich man (Hey, hey, hey, hey)<br>
      (I'ma carry myself) I am a rich man (Hey, hey, hey, hey)<br>
      I'm my own biggest fan and I'm high in demand<br>
      (Hey, hey) I am a rich man (Rich man)</p>

      <p class="lyric-section">[Post-Chorus: All]</p>
      <p>(La-la, la-la, la, ah-ah)<br>
      I am what I am<br>
      (La-la, la-la, la, ah-ah)<br>
      I am a rich man<br>
      (La-la, la-la, la, ah-ah)<br>
      I am what I am<br>
      (La-la, la-la, la, ah-ah)<br>
      I am a rich man</p>

      <p class="lyric-section">[Verse 2: Ningning, Karina, Giselle, Winter]</p>
      <p>Don't care about what they say<br>
      날 밀어내고 함부로 굴 때 오히려,<br>
      okay, see? My name is What my name is<br>
      (I am a rich man)<br>
      Don't need the money, yeah, I see it In my closet, my ideas<br>
      내 말버릇, 내 걸음, 내 이름<br>
      You know when I'm serving them looks, I'ma feed 'em</p>

      <p class="lyric-section">[Pre-Chorus: Karina, Winter & Giselle, Ningning, Giselle]</p>
      <p>딴 생각 말고 self-belief<br>
      'Cause 그게 좀 더 재밌잖아 Ooh-woah, oh<br>
      I am a rich man<br>
      So I am standin', where you lookin'?<br>
      맞춘 듯한 my perfect fit<br>
      Baby<br>
      I am a rich man</p>

      <p class="lyric-section">[Chorus: Giselle, Ningning, Winter, Karina]</p>
      <p>(I'ma carry myself)<br>
      I am a rich man<br>
      (I'ma carry myself)<br>
      I am a rich man<br>
      I'm that one, 난 나로 가득해 by myself<br>
      I am a rich man<br>
      (I'ma carry myself)<br>
      I am a rich man<br>
      (I'ma carry myself)<br>
      I am a rich man<br>
      I'm my own biggest fan and I'm high in demand<br>
      (Say, ooh) I am a rich man</p>

      <p class="lyric-section">[Verse 3: Karina, Giselle]</p>
      <p>Twenty four, 모두가 same shade<br>
      You already know what the tag say<br>
      Make it better on my own, my tag<br>
      I won't double back, 흉내 안 내<br>
      If you blame it, cameo<br>
      I carry the load, run the show<br>
      I'm like a diamond ring,<br>
      already got my thing<br>
      Cannot put a price on it, this is the real deal, yeah</p>

      <p class="lyric-section">[Interlude: Winter]</p>
      <p>I am a rich man</p>

      <p class="lyric-section">[Chorus: Winter, Karina, Ningning, Giselle]</p>
      <p>(I'ma carry myself)<br>
      I am a rich man<br>
      (I'ma carry myself)<br>
      I am a rich man<br>
      I'm that one, 난 나로 가득해 by myself<br>
      (Say, what?) I am a rich man (Hoo)<br>
      (I'ma carry myself)<br>
      I am a rich man<br>
      (Hey, hey, hey, hey)<br>
      (I'ma carry myself)<br>
      I am a rich man<br>
      (Hey, hey, hey, hey)<br>
      I'm my own biggest fan and I'm high in demand<br>
      (Hey, hey, hey, hey) (Woo)<br>
      I am a rich man<br>
      (Rich man)</p>

      <p class="lyric-section">[Post-Chorus: (All), Karina, Giselle, Ningning, Winter]</p>
      <p>(La-la, la-la, la, ah-ah; Hey, hey)<br>
      I am what I am<br>
      (La-la, la-la, la, ah-ah)<br>
      So good, so good, so good<br>
      I am a rich man<br>
      (La-la, la-la, la, ah-ah; Hey, hey)<br>
      I am what I am<br>
      (La-la, la-la, la, ah-ah)<br>
      I am a rich man</p>
    </div>
  </div>

  <div class="right-sidebar-section">
    <div class="producer-box">
      <h4>Credits</h4>
      <p><strong>Producer:</strong> SM Entertainment</p>
      <p><strong>Songwriters:</strong> Yoo Young-jin, Tayla Parx, Mark Feist</p>
    </div>

    <div class="photo-grid">
      <img src="/Projek_PWF/asset/Foto Group Richman (1).png" alt="aespa 1">
      <img src="/Projek_PWF/asset/Solo Shoot Karina.png" alt="aespa 2">
      <img src="/Projek_PWF/asset/Solo Shoot Giselle.png" alt="aespa 3">
      <img src="/Projek_PWF/asset/Solo Shoot Winter.png" alt="aespa 4">
      <img src="/Projek_PWF/asset/Solo Shoot Ningning.png" alt="aespa 5">
    </div>
  </div>

</body>
</html>
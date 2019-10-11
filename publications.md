---
layout: publications
permalink: /publications/
title: Publications
tags: [publications]
modified: 14-7-2016
comments: true
---




<head>
  <meta name=viewport content="width=800">
  <meta name="generator" content="HTML Tidy for Linux/x86 (vers 11 February 2007), see www.w3.org">
  <style type="text/css">
    /* Color scheme stolen from Sergey Karayev */
    
    a {
      color: #1772d0;
      text-decoration: none;
    }
    
    a:focus,
    a:hover {
      color: #f09228;
      text-decoration: none;
    }
    
    body,
    td,
    th,
    tr,
    p,
    a {
      font-family: 'Lato', Verdana, Helvetica, sans-serif;
      font-size: 14px
    }
    
    strong {
      font-family: 'Lato', Verdana, Helvetica, sans-serif;
      font-size: 14px;
    }
    
    heading {
      font-family: 'Lato', Verdana, Helvetica, sans-serif;
      font-size: 22px;
    }
    
    papertitle {
      font-family: 'Lato', Verdana, Helvetica, sans-serif;
      font-size: 14px;
      font-weight: 700
    }
    
    name {
      font-family: 'Lato', Verdana, Helvetica, sans-serif;
      font-size: 32px;
    }
    
    .one {
      width: 160px;
      height: 160px;
      position: relative;
    }
    
    .two {
      width: 160px;
      height: 160px;
      position: absolute;
      transition: opacity .2s ease-in-out;
      -moz-transition: opacity .2s ease-in-out;
      -webkit-transition: opacity .2s ease-in-out;
    }
    
    .fade {
      transition: opacity .2s ease-in-out;
      -moz-transition: opacity .2s ease-in-out;
      -webkit-transition: opacity .2s ease-in-out;
    }
    
    span.highlight {
      background-color: #ffffd0;
    }
  </style>
  <link rel="icon" type="image/png" href="images/seal_icon.png">
  <title>Fahad Shamshad</title>
  <meta http-equiv="Content-Type" content="text/html; charset=us-ascii">
  <link href='https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
</head>

<body>
  <table width="800" border="0" align="center" cellspacing="0" cellpadding="0">
    <tr>
      <td>

		
        <table width="100%" align="center" border="0" cellspacing="0" cellpadding="20">
          <tr>
            <td width="100%" valign="middle">
              <heading>Research</heading>
              <p>
                I am interested in computational imaging, machine learning, optimization, and image processing.. Much of my recent research is about regularizing the inverse problems in signal and image processing using generative models (GANs, VAEs and Intertible models). Before that i have worked on theoretical aspect of samling architectures designed for low rank and sparse signals. I have also worked on removing Poisson noise in low light imaging in astronomy.
              </p>
            </td>
          </tr>
        </table>

        <table width="120%" align="center" border="0" cellspacing="0" cellpadding="20">
          
          <tr>
            <td width="25%">
              <img src='images/BD.PNG'>
            </td>
            <td valign="top" width="75%">
              <p>
                <a href="https://arxiv.org/abs/1701.03077">
                  <papertitle>Blind Image Deconvolution using Pretrained Generative Priors</papertitle>
                </a>
                <br>
                Muhammad Asim*, <strong> Fahad Shamshad* </strong>, Ali Ahmed
                <br>
                <em>Submitted to 'Which-Must-Not-Be-Named'</em>, 2019
                <br>
                <p></p>
                <p>This paper proposes a novel approach to regularize the ill-posed and non-linear blind image deconvolution (blind deblurring) problem using deep generative networks</p>
            </td>
          </tr>
          
          <tr onmouseout="portrait_stop()" onmouseover="portrait_start()">
            <td width="25%">
              <div class="one">
                <div class="two" id='portrait_image'><img src='images/BD-J.PNG'></div>
                <img src='images/BD-J-after.PNG'>
              </div>
              <script type="text/javascript">
                function portrait_start() {
                  document.getElementById('portrait_image').style.opacity = "1";
                }
                function portrait_stop() {
                  document.getElementById('portrait_image').style.opacity = "0";
                }
                portrait_stop()
              </script>
            </td>
            <td valign="top" width="25%">
              <a href="https://drive.google.com/file/d/13i6DlS9UhGVKmwslLUFnKBwdxFRVQeQj/view?usp=sharing">
                <papertitle>Blind Image Deconvolution using Deep Generative Priors</papertitle>
              </a>
              <br>
              <a href="http://people.csail.mit.edu/nwadhwa/">Muhammad Asim*</a>,
              <a href="http://rahuldotgarg.appspot.com/"> <strong>Fahad Shamshad* </strong></a>,
              <a href="http://www.cs.cmu.edu/~ymovshov/">Ali Ahmed</a>,
              <br>
              <em>Submitted to TPAMI</em>, 2018
              <br>
              <a href="https://arxiv.org/abs/1806.04171">arxiv</a> /
              <a href="https://ai.googleblog.com/2017/10/portrait-mode-on-pixel-2-and-pixel-2-xl.html">blog post</a> /
              <a href="data/Wadhwa2018.bib">bibtex</a>
              <p></p>
              <p>In this paper, we employ generative models to regularize highly ill-posed blind image deblurring problem.</p>
            </td>
          </tr>

          <tr onmouseout="aperture_stop()" onmouseover="aperture_start()">
            <td width="25%">
              <div class="one">
                <div class="two" id='aperture_image'><img src='images/ptych.PNG'></div>
                <img src='images/ptych.PNG'>
              </div>
              <script type="text/javascript">
                function aperture_start() {
                  document.getElementById('aperture_image').style.opacity = "1";
                }
                function aperture_stop() {
                  document.getElementById('aperture_image').style.opacity = "0";
                }
                aperture_stop()
              </script>
            </td>
            <td valign="top" width="75%">
              <a href="https://drive.google.com/open?id=1MpvxcW7OTJP321QL_q4ZLQ8D653bZZzy">
                <papertitle>Deep Ptych: Subsampled Fourier Ptychography using Generative Priors</papertitle>
              </a>
              <br>
              <a href="https://people.eecs.berkeley.edu/~pratul/">Fahad Shamshad</a>,
              <a href="http://rahuldotgarg.appspot.com/">Farwa Abbas</a>,
              <a href="http://people.csail.mit.edu/nwadhwa/">Ali Ahmed</a>,
              <br>
              <em>Submitted to ICASSP</em>, 2019
              <br>
              <a href="https://github.com/google/aperture_supervision">code</a> /
              <a href="data/Srinivasan2018.bib">bibtex</a>
              <p></p>
              <p>We propose robust ptychography algorithm that acheive comparable reconstruction results to state of the art at low subsampling ratios.</p>
            </td>
          </tr>

          <tr onmouseout="deepburst_stop()" onmouseover="deepburst_start()">
            <td width="25%">
              <div class="one">
                <div class="two" id='deepburst_image'><img src='images/mcs.PNG'></div>
                <img src='images/mcs.PNG'>
              </div>
              <script type="text/javascript">
                function deepburst_start() {
                  document.getElementById('deepburst_image').style.opacity = "1";
                }
                function deepburst_stop() {
                  document.getElementById('deepburst_image').style.opacity = "0";
                }
                deepburst_stop()
              </script>
            </td>
            <td valign="top" width="75%">
              <a href="https://drive.google.com/file/d/1GAH8ijyZ7GnoBnQFANEzdXinHrE4vvXn/view?usp=sharing">
                <papertitle>Poisson Denoising for Astronomical Images</papertitle>
              </a>
              <br>
              <a href="https://people.eecs.berkeley.edu/~bmild/"><strong>Fahad Shamshad</strong></a>,
              <a href="http://people.csail.mit.edu/jiawen/">Mohsin Riaz</a>,
              <a href="http://www.dsharlet.com/">Abdul Ghafoor</a>,
              <br>
              <em>Advances in Astronomy</em>, 2018 &nbsp <font color=#FF8080><strong>(Spotlight)</strong></font>
              <br>
              <a href="https://drive.google.com/file/d/1aqk3Q-L2spjLZh2yRWKUWIDcZkGjQ7US/view?usp=sharing">supplement</a> /
              <p></p>
              <p>The scheme employs the concept of Exponential Principal Component Analysis and sparsity of image patches to remove high Poisson noise from astronomical images.</p>
            </td>
          </tr>

          <tr onmouseout="friendly_stop()" onmouseover="friendly_start()">
            <td width="25%">
              <div class="one">
                <div class="two" id='friendly_image'><img src='images/phase.PNG'></div>
                <img src='images/phase.PNG'>
              </div>
              <script type="text/javascript">
                function friendly_start() {
                  document.getElementById('friendly_image').style.opacity = "1";
                }
                function friendly_stop() {
                  document.getElementById('friendly_image').style.opacity = "0";
                }
                friendly_stop()
              </script>
            </td>
            <td valign="top" width="75%">
              <p>
                <a href="https://drive.google.com/file/d/1w_0djhL0QgC_fbehnJ0c-J23_kW_420p/view?usp=sharing">
                  <papertitle>Robust Compressive Phase Retrieval using Generative Priors</papertitle>
                </a>
                <br>
                 <a href="https://people.eecs.berkeley.edu/~bmild/"><strong>Fahad Shamshad</strong></a>,
                 <a href="http://people.csail.mit.edu/jiawen/">Ali Ahmed</a>,
                <br>
                <em>To be submitted to IEEE Transaction on Computational Imaging</em>, 2018
                <br>
                <a href="https://sampa.cs.washington.edu/projects/vr-hw.html">project page</a>
                <p></p>
                <p>This paper proposes a new framework to regularize the highly ill-posed and non-linear phase retrieval problem through deep generative priors using simple gradient descent algorithm.p>
            </td>
          </tr>

         
        </table>

        <script type="text/javascript">
          var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
          document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
        </script>
        <script type="text/javascript">
          try {
            var pageTracker = _gat._getTracker("UA-7580334-1");
            pageTracker._trackPageview();
          } catch (err) {}
        </script>
        </td>
    </tr>
  </table>
</body>

</html>

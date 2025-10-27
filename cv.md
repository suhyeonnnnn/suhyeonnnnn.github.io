---
layout: minimal_base
title: "CV"
---

<div class="content" style="padding: 0;">
    <!-- CV 헤더 -->


    <!-- PDF 뷰어 -->
    <div style="height: calc(100vh - 200px); min-height: 800px; background: #f5f5f5;">
        <iframe src="/assets/files/SuhyeonLee_CV.pdf" 
                width="100%" 
                height="100%" 
                style="border: none; background: white;"
                title="Suhyeon Lee CV">
            <div style="padding: 2rem; text-align: center;">
                <p style="margin-bottom: 1rem; color: var(--text-secondary);">
                    Your browser doesn't support PDF viewing. 
                </p>
                <a href="/assets/files/SuhyeonLee_CV.pdf" 
                   download="SuhyeonLee_CV.pdf"
                   style="background: var(--accent-color); color: white; padding: 1rem 2rem; border-radius: 10px; text-decoration: none; font-weight: 500;">
                    📄 Download PDF instead
                </a>
            </div>
        </iframe>
    </div>

    <!-- 모바일용 대체 뷰 -->
    <div id="mobile-fallback" style="display: none; padding: 2rem; text-align: center;">
        <div style="background: rgba(0, 0, 0, 0.02); padding: 2rem; border-radius: 15px; max-width: 500px; margin: 0 auto;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
            <h3 style="margin-bottom: 1rem; color: var(--text-primary);">CV Document</h3>
            <p style="margin-bottom: 2rem; color: var(--text-secondary);">
                View my complete curriculum vitae by downloading the PDF file below.
            </p>
            <a href="/assets/files/SuhyeonLee_CV.pdf" 
               download="SuhyeonLee_CV.pdf"
               style="background: var(--accent-color); color: white; padding: 1rem 2rem; border-radius: 10px; text-decoration: none; font-weight: 500; display: inline-block;">
                📄 Download CV (PDF)
            </a>
        </div>
    </div>
</div>

<script>
// 모바일에서 PDF 뷰어 대신 다운로드 링크 표시
function checkMobile() {
    if (window.innerWidth <= 768) {
        document.querySelector('iframe').style.display = 'none';
        document.getElementById('mobile-fallback').style.display = 'block';
    } else {
        document.querySelector('iframe').style.display = 'block';
        document.getElementById('mobile-fallback').style.display = 'none';
    }
}

// 페이지 로드 시와 창 크기 변경 시 체크
window.addEventListener('load', checkMobile);
window.addEventListener('resize', checkMobile);
</script>

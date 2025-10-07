import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# === 기본 설정 ===
frames = 48           # 24fps × 2초 루프
size = 512
radius = 1.0

# === 구의 좌표 생성 ===
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
x = radius * np.sin(theta) * np.cos(phi)
y = radius * np.sin(theta) * np.sin(phi)
z = radius * np.cos(theta)

# === 색상 그라데이션 (파스텔) - SVG 색상 기반 ===
def pastel_gradient(x, y, z):
    # 하늘색 → 보라 → 핑크 → 코랄 그라데이션
    # z 좌표를 기준으로 색상 매핑
    norm_z = (z + 1) / 2  # -1~1을 0~1로 정규화
    
    # SVG에서 가져온 색상들 (RGB 정규화)
    sky_blue = np.array([0.74, 0.85, 0.93])     # #BDD9EE
    purple = np.array([0.75, 0.71, 0.82])       # #BEB5D2  
    pink = np.array([0.96, 0.78, 0.83])         # #FCBBCB
    coral = np.array([0.98, 0.61, 0.56])        # #FC9C8E
    
    # 4단계 그라데이션
    colors = np.zeros((*z.shape, 3))
    
    # 각 픽셀에 대해 색상 보간
    for i in range(z.shape[0]):
        for j in range(z.shape[1]):
            t = norm_z[i, j]
            if t < 0.33:
                # 하늘색 → 보라
                blend = t * 3
                colors[i, j] = (1 - blend) * sky_blue + blend * purple
            elif t < 0.66:
                # 보라 → 핑크
                blend = (t - 0.33) * 3
                colors[i, j] = (1 - blend) * purple + blend * pink
            else:
                # 핑크 → 코랄
                blend = (t - 0.66) * 3
                colors[i, j] = (1 - blend) * pink + blend * coral
    
    return np.clip(colors, 0, 1)

# 초기 색상 계산
colors = pastel_gradient(x, y, z)

# === 애니메이션 설정 ===
fig = plt.figure(figsize=(size/100, size/100), dpi=100)
fig.patch.set_facecolor('none')  # 투명 배경
ax = fig.add_subplot(111, projection='3d')
ax.axis('off')
ax.set_facecolor('none')

# 구 표면 생성
surf = ax.plot_surface(x, y, z, facecolors=colors, 
                      linewidth=0, antialiased=True, 
                      shade=False, alpha=1.0)

# 축 범위 설정
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)

def animate(frame):
    """애니메이션 함수 - 완전한 360도 회전"""
    # 대각선 회전을 위한 각도 계산
    angle = frame * 360 / frames  # 0도부터 360도까지 완전 회전
    
    # 대각선 회전: Y축 회전 + 약간의 X축 회전
    elev = 20 + 15 * np.sin(np.radians(angle * 0.5))  # 부드러운 상하 움직임
    azim = angle  # 메인 회전
    
    ax.view_init(elev=elev, azim=azim)
    
    return [surf]

# === 애니메이션 생성 ===
print("🎬 애니메이션 생성 중...")
anim = FuncAnimation(fig, animate, frames=frames, 
                    interval=1000//24, blit=True, repeat=True)

# === GIF 저장 ===
print("💾 GIF 저장 중...")
writer = PillowWriter(fps=24)
plt.tight_layout()

# 투명 배경으로 저장
anim.save("fixed_pastel_sphere.gif", writer=writer, dpi=100, 
         savefig_kwargs={"transparent": True, "facecolor": "none"})

print("✅ 완성! 파일명: fixed_pastel_sphere.gif")
print("📋 설정:")
print(f"   • 크기: {size}x{size}")
print(f"   • 프레임: {frames}개 (2초 루프)")
print(f"   • FPS: 24")
print(f"   • 회전: 완전한 360도 대각선 회전")
print(f"   • 배경: 투명")

plt.show()  # 미리보기 (선택사항)
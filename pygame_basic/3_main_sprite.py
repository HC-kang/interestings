import pygame

pygame.init() # 초기화(반드시 실시해야함)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 
pygame.display.set_caption('Nado game') # 게임 이름 

# 배경이미지 불러오기
background = pygame.image.load('/Users/heechankang/projects/pygame_basic/TEST.jpg')

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load('')



# 프로그램 실행은 되지만 내용이 없어서 바로 꺼짐.
# 이벤트 루프   
running = True # 게임이 진행 중
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 실행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임화면 계속 그리기

# pygame 종료
pygame.quit()


import pygame
import random
import sys
from tkinter import messagebox, Tk

# 1. 프로젝트 설정 (명세서 기준) [cite: 25, 145, 181]
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20  # 격자 한 칸의 크기 (20x20 pixel) [cite: 146, 147]
FPS = 5  # 뱀의 이동 속도

# 색상 정의 [cite: 32, 47, 146]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)    # 먹이 색상 [cite: 47, 170]
GREEN = (0, 255, 0)  # 뱀 색상 [cite: 32, 180]

class SnakeGame:
    def __init__(self):
        pygame.init()
        # Tkinter 초기화 (메시지 박스용) [cite: 234]
        self.root = Tk()
        self.root.withdraw()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        # 뱀 초기화: 랜덤 위치 및 랜덤 방향 설정 [cite: 34, 35, 180]
        # 즉사 방지를 위해 중앙 부근(격자 단위)에서 시작하도록 설정
        start_x = random.randint(5, 14) * BLOCK_SIZE
        start_y = random.randint(5, 14) * BLOCK_SIZE
        self.snake = [(start_x, start_y)]
        
        # 상, 하, 좌, 우 랜덤 방향 설정 [cite: 35]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.food = self.create_food()
        self.game_over = False

    def create_food(self):
        # 먹이 생성: 뱀의 위치와 중복되지 않는 랜덤 위치 [cite: 48, 164, 207]
        while True:
            food_x = random.randint(0, 19) * BLOCK_SIZE
            food_y = random.randint(0, 19) * BLOCK_SIZE
            pos = (food_x, food_y)
            if pos not in self.snake:
                return pos

    def handle_events(self):
        # 키보드 입력 처리 [cite: 53, 54, 182]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    # 현재 진행 방향의 반대 방향으로 즉시 꺾이지 않도록 방지 로직 (선택 사항)
                    if (event.key == pygame.K_UP and self.direction != pygame.K_DOWN) or \
                       (event.key == pygame.K_DOWN and self.direction != pygame.K_UP) or \
                       (event.key == pygame.K_LEFT and self.direction != pygame.K_RIGHT) or \
                       (event.key == pygame.K_RIGHT and self.direction != pygame.K_LEFT):
                        self.direction = event.key

    def update(self):
        # 뱀 머리 이동 로직 [cite: 52, 181, 446]
        cur_x, cur_y = self.snake[0]
        if self.direction == pygame.K_UP: cur_y -= BLOCK_SIZE
        elif self.direction == pygame.K_DOWN: cur_y += BLOCK_SIZE
        elif self.direction == pygame.K_LEFT: cur_x -= BLOCK_SIZE
        elif self.direction == pygame.K_RIGHT: cur_x += BLOCK_SIZE

        new_head = (cur_x, cur_y)

        # 게임 오버 조건 체크: 화면 밖 혹은 자신의 몸에 닿음 [cite: 66, 232, 233, 469, 470]
        if (cur_x < 0 or cur_x >= SCREEN_WIDTH or 
            cur_y < 0 or cur_y >= SCREEN_HEIGHT or 
            new_head in self.snake):
            self.game_over = True
            # 메시지 창 띄우기 [cite: 66, 234, 472]
            messagebox.showinfo("Snake Game", "게임 오버입니다.")
            # 확인 버튼 클릭 후 재시작 (위치 및 먹이 초기화) [cite: 67, 235]
            self.reset()
            return

        # 뱀 리스트 앞에 새로운 머리 추가 [cite: 446, 497]
        self.snake.insert(0, new_head)

        # 먹이를 먹었는지 확인 [cite: 32, 206, 221]
        if new_head == self.food:
            self.food = self.create_food() # 먹이 재설정 [cite: 165, 207]
        else:
            # 먹이를 먹지 않았다면 마지막 꼬리 제거 (이동 효과) [cite: 447, 458, 497]
            self.snake.pop()

    def draw(self):
        self.screen.fill(WHITE)
        
        # 1. 그리드(격자 무늬) 그리기 [cite: 25, 26, 146, 330]
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            pygame.draw.line(self.screen, BLACK, (0, y), (SCREEN_WIDTH, y))

        # 2. 먹이 그리기 (붉은색 사각형) [cite: 47, 163, 170]
        pygame.draw.rect(self.screen, RED, (*self.food, BLOCK_SIZE, BLOCK_SIZE))

        # 3. 뱀 그리기 (초록색 사각형) [cite: 32, 180, 389]
        for part in self.snake:
            pygame.draw.rect(self.screen, GREEN, (*part, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.update()

    def play(self):
        # 메인 게임 루프 [cite: 19]
        while True:
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = SnakeGame()
    game.play()
import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 780, 580
SIZE = 22
BACKGROUND_COLOR = (0, 255, 0)
SNAKE_COLOR = (255, 0, 255) 
FONT_COLOR = (255, 255, 255)  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()

def generate_ball(snake):
    ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while True:
        ball_position = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))
        if ball_position not in snake:
            return ball_position, ball_color

def main():
    snake = [(0, 0), (0, SIZE), (0, 2 * SIZE)]
    direction = (0, SIZE)
    ball, ball_color = generate_ball(snake)
    score = 0
    
    font = pygame.font.SysFont(None, 30) 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -SIZE)
                elif event.key == pygame.K_DOWN:
                    direction = (0, SIZE)
                elif event.key == pygame.K_LEFT:
                    direction = (-SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (SIZE, 0)
                elif event.key == pygame.K_RETURN:  
                    pygame.quit()
                    sys.exit()

        head_position = snake[0]
        new_head = (head_position[0] + direction[0], head_position[1] + direction[1])
        snake.insert(0, new_head)

        if snake[0] == ball:
            ball, ball_color = generate_ball(snake)
            score += 1
        else:
            snake.pop()

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, ball_color, pygame.Rect(ball[0], ball[1], SIZE, SIZE))
        for pos in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], SIZE, SIZE))
        
        text = font.render(f"Score: {score}", True, FONT_COLOR)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
    #123
    
import pygame
import numpy as np

pygame.init()

# Screen variables
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

finishGame = False

# Draw variables
borderY0 = pygame.Rect(((SCREEN_HEIGHT/3)-25, 0, 50, SCREEN_HEIGHT))
borderY1 = pygame.Rect((2*(SCREEN_HEIGHT/3)-25, 0, 50, SCREEN_HEIGHT))
borderX0 = pygame.Rect((0, (SCREEN_HEIGHT/3)-25, SCREEN_WIDTH, 50))
borderX1 = pygame.Rect((0, 2*(SCREEN_HEIGHT/3)-25, SCREEN_WIDTH, 50))
borders = [borderY0, borderX0, borderX1, borderY1]
blueMarks = []
redMarks = []

# Board variables
board = np.array([[0,0,0],[0,0,0],[0,0,0]])

# Turn 1=blue, -1=red
turn = 1
turnDict = {1: "BLUE", -1: "RED"}

# Text font and draw text
text_font = pygame.font.SysFont("Consolas", 30)

def draw_text(text, font, color, x, y):
    textcontent = font.render(text, True, color)
    textbox = pygame.Rect(((SCREEN_WIDTH/2)-250, (SCREEN_HEIGHT/2)-250, 500, 500))
    pygame.draw.rect(screen, (255, 255, 255), textbox)
    screen.blit(textcontent, (x-textcontent.get_width()//2,y-textcontent.get_height()//2))

# Draw a blue circle or a red square
def mark(i, j, turn):
    if board[j][i] == 0:
        if turn == 1:
            blueMarks.append([i,j,100])
            if len(blueMarks) > 3:
                removeMark = blueMarks[0]
                board[removeMark[1]][removeMark[0]] = 0
                blueMarks.remove(removeMark)
        else:
            redMarks.append([i,j,200])
            if len(redMarks) > 3:
                removeMark = redMarks[0]
                board[removeMark[1]][removeMark[0]] = 0
                redMarks.remove(removeMark)
        board[j][i] = turn
        turn = -turn
    return turn

# Check if someone wins
def win(finishGame):
    for row in range(len(board)):
        if abs(sum(board[row])) == 3:
            draw_text(turnDict[board[row][0]]+" wins!!!", text_font, (0,0,0), SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            finishGame = True
            break
        elif abs(sum(board[:,row])) == 3:
            draw_text(turnDict[board[0][row]]+" wins!!!", text_font, (0,0,0), SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            finishGame = True
            break
        elif abs(sum(board.diagonal())) == 3:
            draw_text(turnDict[board[0][0]]+" wins!!!", text_font, (0,0,0), SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            finishGame = True
            break
        elif abs(sum(np.fliplr(board).diagonal())) == 3:
            draw_text(turnDict[board[0][2]]+" wins!!!", text_font, (0,0,0), SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            finishGame = True
            break
    return finishGame

# Game loop
run = True
while run:

    screen.fill((0,0,0))

    # Draw borders
    for brd in borders:
        pygame.draw.rect(screen, (255, 255, 255), brd)

    # Draw blue marks
    for m in blueMarks:
        pygame.draw.circle(screen, (0, 0, 255), (m[0]*300+150, m[1]*300+150), m[2])
        pygame.draw.circle(screen, (0, 0, 0), (m[0]*300+150, m[1]*300+150), m[2]-25)

    # Draw red marks
    for m in redMarks:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((m[0]*300+50, m[1]*300+50, m[2], m[2])))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((m[0]*300+75, m[1]*300+75, m[2]-50, m[2]-50)))

    finishGame = win(finishGame)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP and not finishGame:
            clickPos = pygame.mouse.get_pos()
        
            i = 0
            j = 0

            # Convert coords to matrix positions (i j): i = x = col, j = y = row
            if clickPos[0] > 300:
                if clickPos[0] > 600:
                    i = 2
                else:
                    i = 1
            if clickPos[1] > 300:
                if clickPos[1] > 600:
                    j = 2
                else:
                    j = 1 

            turn = mark(i,j, turn)

    pygame.display.update()
pygame.quit()
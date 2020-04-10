import pygame
import config as conf
from gamestate import GameState
from models.HeuristicModel import HeuristicModel
from models.RandomModel import RandomModel
from models.DQNModel import DQNModel

game = GameState()

# main game loop
game.init_manual_agent('AgarAI')
# game.init_ai_agents(conf.NUM_AI)
game.init_ai_agents(1, RandomModel(5, 10), 'Random')
game.init_ai_agents(1, HeuristicModel(), 'Heuristic')
game.main_loop()

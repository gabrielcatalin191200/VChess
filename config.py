# Written By: davidADSP 
# Minor Changes By: Tindur Sigurdason & Calen Irwin

# Reference:
# https://github.com/AppliedDataSciencePartners/DeepReinforcementLearning/blob/master/config.py

#### SELF PLAY
EPISODES = 5
MCTS_SIMS = 20
MEMORY_SIZE = int(3e3)
TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

HIDDEN_CNN_LAYERS = [
	{'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
   	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
   	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
   	  , {'filters':256, 'kernel_size': (3, 3)}
      , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
	  , {'filters':256, 'kernel_size': (3, 3)}
   	  , {'filters':256, 'kernel_size': (3, 3)}
	]

#### EVALUATION
EVAL_EPISODES = 6
SCORING_THRESHOLD = 55/45
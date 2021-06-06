# Conditional Text Generation with CTRL

The work mainly relies on the usage of three bash scripts, whose function will be briefly explained below. There are two version for each script: one for the 48 layer model and one for the 36 layer model (which is specified by the '36' in its name).

## initialize.sh (or initialize36.sh)

Creates a folder to store all the files, creates the virtual environment e activates it, installs all the packages required by the model.

No argument is required to be passed.

## training.sh (or training36.sh)
Takes a *txt* dataset, creates the Tensorflow record file and performs the training on it.

It is meant to be placed into the project folder created in the previous step (together with *ctrl* and *venv* folders).

It requires 5 arguments.

The first argument is the name of the dataset *txt* file (to be placed into the *training_utils* folder).

The second argument is the control code to which the dataset refers to.

The third argument is the number of iterations (epochs).

The fourth argument (optional) is the learning rate of the optimizer (it is set to 1e-2 by default).

## generation.sh (or generation36.sh)
Starting from a checkpoint, it runs the generation step.

It is meant to be placed into the project folder created in the first step (together with *ctrl* and *venv* folders).

It requires 7 arguments.

The first argument is the *temperature* parameter.

The second argument is the *top-k* parameter.

The third argument is the *generate_num* parameter, the number of tokens to be generated for each sentence.

The fourth argument is the *n_sentences* parameter, the number of sentences to be generated starting from each prompt.

The fifth argument is the *nucleus* parameter.

The sixth argument is the prompt list, a *txt* file with one prompt per line.

The seventh argument (optional) is the output *txt* file (it is set to '*output.txt*' by default).
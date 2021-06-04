import os
import numpy as np

# Acessando variáveis de ambiente de dentro do Container
print(os.environ.get("ENV_VAR_COMPOSE"))
print(os.environ.get("ENV_VAR_DOCKERFILE"))
print(os.environ.get("ENV_ARG"))

# Utilizando a biblioteca numpy instalada pelo Dockerfile
a = np.array([2,3,4])
print(a)

print("It's Works!")
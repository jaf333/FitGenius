# FitGenius
**Personalized fitness and supplement recommendations powered by AI**

## Descripción

**FitGenius** es una plataforma innovadora diseñada para ayudar a las personas a optimizar sus rutinas de ejercicio y suplementación deportiva. Utilizando algoritmos de inteligencia artificial, FitGenius ofrece recomendaciones personalizadas basadas en tus objetivos y preferencias.

## Características

- **Recomendaciones de suplementos**: Obtén sugerencias sobre los mejores suplementos deportivos adaptados a tus necesidades específicas.
- **Rutinas de ejercicio personalizadas**: Accede a planes de entrenamiento diseñados para ayudarte a alcanzar tus objetivos de fitness.
- **Seguimiento y ajustes**: Monitorea tu progreso y recibe ajustes en tiempo real para maximizar tus resultados.

## Endpoints

- `GET /api/recommend/?user_id=1`: Get personalized supplement recommendations.
- `GET /api/exercises/`: Get a list of exercises from the Wger API.
- `GET /api/exercises/<int:exercise_id>/`: Get details of a specific exercise by its ID.
- `POST /api/authenticated_exercises/`: Get a list of authenticated exercises using JWT. (requires `username` and `password` in the request body)



CREATE DATABASE profiles_db;

-- Conectar a la base de datos recién creada
\c profiles_db;

-- Crear la tabla de usuarios si no existe
CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    public_info VARCHAR(255) NOT NULL,
    messaging VARCHAR(255) NOT NULL,
    biography VARCHAR(255) NOT NULL,
    organization VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    social_media VARCHAR(255) NOT NULL,
    email VARCHAR(255)
);

INSERT INTO profiles (name, url, nickname, public_info, messaging, biography, organization, country, social_media, email) VALUES 
('Juan', 'http://example.com/juan', 'juanjr', 'Hola, soy Juan', 'Telegram: @juan', '¡Hola! Soy Juan, un entusiasta de la vida.', 'OpenAI', 'Mexico', 'twitter.com/juanjr', 'juan@email.com'),
('Pedro', 'http://example.com/pedro', 'pedro_g', '¡Hola a todos!', 'Telegram: @pedro_g', 'Me encanta la naturaleza y la música.', 'Tech Solutions', 'Spain', 'instagram.com/pedro_g', 'pedro@email.com'),
('Luis', 'http://example.com/luis', 'lui5', 'Bienvenidos a mi perfil', 'WhatsApp: +123456789', 'Programador apasionado y aficionado al deporte.', 'TechCo', 'Argentina', 'facebook.com/lui5', 'luis@email.com'),
('Diego', 'http://example.com/diego', 'digo_d', '¡Hola mundo!', 'WhatsApp: +987654321', 'Me gusta viajar y descubrir nuevas culturas.', 'Travel Agency', 'Colombia', 'linkedin.com/in/digo_d', 'diego@email.com'),
('Carlos', 'http://example.com/carlos', 'c4r', '¡Saludos a todos!', 'Telegram: @c4r', 'Ingeniero de software con pasión por los juegos de mesa.', 'GameDev', 'Chile', 'github.com/c4r', 'carlos@email.com'),
('Sofía', 'http://example.com/sofia', 'sofia_23', '¡Hola a todos!', 'WhatsApp: +1122334455', 'Amante del cine y la literatura.', 'Media Company', 'Peru', 'twitter.com/sofia_23', 'sofia@email.com'),
('Ana', 'http://example.com/ana', 'ana_a', '¡Bienvenidos!', 'Telegram: @ana_a', 'Apasionada por la tecnología y la música.', 'Tech Startup', 'Brazil', 'linkedin.com/in/ana_a', 'ana@email.com'),
('María', 'http://example.com/maria', 'mariamtz', '¡Hola a todos!', 'WhatsApp: +5544332211', 'Viajera empedernida y amante de los animales.', 'Non-Profit Organization', 'Mexico', 'instagram.com/mariamtz', 'maria@email.com'),
('Lucía', 'http://example.com/lucia', 'lucialucia', '¡Saludos!', 'Telegram: @lucialucia', 'Me gusta el arte y la fotografía.', 'Art Gallery', 'Spain', 'facebook.com/lucialucia', 'lucia@email.com'),
('Miguel', 'http://example.com/miguel', 'mike_air', '¡Hola mundo!', 'WhatsApp: +987654321', 'Entusiasta del deporte y la vida al aire libre.', 'Fitness Center', 'Colombia', 'twitter.com/mike_air', 'miguel@email.com'),
('Andrés', 'http://example.com/andres', 'andres_f', '¡Bienvenidos a mi perfil!', 'Telegram: @andres_f', 'Amante de la gastronomía y los viajes.', 'Food Blogger', 'Chile', 'instagram.com/andres_f', 'andres@email.com');

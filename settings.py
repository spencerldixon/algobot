import dotenv

dotenv.load()

# Service Variables
fxcm_username   = dotenv.get('FXCM_USERNAME',   default='123456789')
fxcm_password   = dotenv.get('FXCM_PASSWORD',   default='password123')
fxcm_account    = dotenv.get('FXCM_ACCOUNT',    default='Real')
pg_database     = dotenv.get('PG_DATABASE',     default='algodb')
pg_username     = dotenv.get('PG_USERNAME',     default='postgres')
pg_password     = dotenv.get('PG_PASSWORD',     default='pass1234')
pg_host         = dotenv.get('PG_HOST',         default='127.0.0.1')
pg_port         = dotenv.get('PG_POST',         default='5432')

# Algobot Config
currencies  = ["GBP/USD", "NZD/CAD"]
time_frames = ["1d", "8hr", "2hr"]

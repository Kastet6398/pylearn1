import cloudinary
import cloudinary.uploader
cloudinary.config( 
  cloud_name = "dkmvoezsb", 
  api_key = "453639488567156", 
  api_secret = "VerqaZWCdO2tioT2EBLb3dn0hrM" 
)

cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", 
  public_id = "olympic_flag")

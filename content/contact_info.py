from utils import img_html

linkedin = img_html('media/logo-linkedin.png', 'max-width:32px', '')
github = img_html('media/logo-github.png', 'max-width:32px', '')
facebook = img_html('media/logo-fb.png', 'max-width:32px', '')
instagram = img_html('media/logo-instagram.png', 'max-width:32px', '')
email = img_html('media/logo-email.png', 'max-width:32px', '')

socia_media_links = f"""
    <div style='text-align:center;'>
        <div style='inline-block'>
        <a href='mailto:adilet.gaparov@gmail.com' style='margin-right:5px'>{email}</a>
        <a href="http://www.linkedin.com/in/adilet-gaparov" target= '_blank' style='margin:5px'>{linkedin}</a>
        <a href="http://www.github.com/adiletgaparov" target= '_blank' style='margin:5px'>{github}</a>
        <a href="http://www.facebook.com/adiletgaparov" target='_blank' style='margin:5px'>{facebook}</a>
        <a href="http://www.instagram.com/adilet.gaparov" target='_blank' style='margin:5px'>{instagram}</a>
        </div>
    </div>
    """
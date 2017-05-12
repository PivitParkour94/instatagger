from instapy import InstaPy

#if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment

print("InstaTagger!!")
session = InstaPy(username='###############', password='###########*')
loggedIn = session.login()
if loggedIn:
    print("It worked!")
else:
    print("couldn't log in! loggedIn.user {1}".format(str(loggedIn)))

#likes specified amount of posts for each hashtag in the array (the '#' is optional)
#in this case: 100 dog-posts and 100 cat-posts
session.like_by_tags(['#dog', 'cat'], amount=100)

#gets tags from image passed as instagram-url and likes specified amount of images for each tag
session.like_from_image(url='www.instagram.com/p/BSrfITEFUAM/', amount=100)

#likes 50 photos of other animals

session.like_by_tags(['#animals'], amount=50, media='Photo')
session.like_from_image(url='www.instagram.com/image', amount=50, media='Photo')

#likes 15 videos of cats

session.like_by_tags(['#cat'], amount=15, media='Video')
session.like_from_image(url='www.instagram.com/image', amount=15, media='Video')

session.end()
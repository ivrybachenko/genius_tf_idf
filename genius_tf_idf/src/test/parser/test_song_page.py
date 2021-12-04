import unittest

from parser.page import SongPage


class SearchResultPageTestCase(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        with open('data/song_page.html', 'r') as f:
            self.song_page_html = f.read()

    def test_get_text(self):
        parser = SongPage(self.song_page_html)
        expected_text = """[Verse 1]
It's funny how the whiskey eases the pain
And softens her words rollin' 'round in my brain
Instead of "I'm leavin'," she says "I'll be back in a little while"
So, hey there, bartender, you better hang close
'Cause I'm lookin' for answers in that bottle you hold
The truth is it's over, but oh what the hell?
If I want to go on and lie to myself

[Chorus]
That's what's workin' right now and I'm gonna take it
As far as I need to 'til my heart can make it
Through one single night without thinkin' of her
And wakin' up lonely, but until that occurs
I'll just sit here and drink 'til I drown
'Cause that's what's workin' right now

[Verse 2]
I tried staying home after she left
But there's too many memories for me to forget
And every room is haunted
By a ghost that once said that she loved me
So I found a place where grown men can hide
And not be ashamed if he breaks down and cries
I know I should go home, but I know what's in store
Hey, and who gives a damn if I just have one more?

[Chorus]
That's what's workin' right now and I'm gonna take it
As far as I need to 'til my heart can make it
Through one single night without thinkin' of her
And wakin' up lonely, but until that occurs
I'll just sit here and drink 'til I drown
'Cause that's what's workin' right now, oh

[Chorus]
That's what's workin' right now and I'm gonna take it
As far as I need to 'til my heart can make it
Through one single night without thinkin' of her
And wakin' up lonely, but until that occurs
I'll just sit here and drink 'til I drown
I'll just sit here and drink 'til I drown
I'll just sit here and drink 'til I drown
'Cause that's what's workin' right now"""
        self.assertEqual(expected_text, parser.get_text())

    def test_get_song_name(self):
        parser = SongPage(self.song_page_html)
        self.assertEqual('That’s What’s Working Right Now', parser.get_song_name())

    def test_get_artist_name(self):
        parser = SongPage(self.song_page_html)
        self.assertEqual('Trent Tomlinson', parser.get_artist_name())
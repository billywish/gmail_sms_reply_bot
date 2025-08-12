import datetime
import random
import time


class LyricPrinter:

    def __init__(self, song_dicts):
        # list of dictionaries
        # song_dicts = [{
        #     "title": "Song title",
        #     "section": "chorus",
        #     "lyrics": "What a wonderful world",
        #     "duration": datetime.timedelta(minutes=1, seconds=20)
        # }]
        self.song_dicts = song_dicts
        self.time_elapsed_for_current_section = datetime.timedelta(seconds=0)
        self.patterns_index = 0
        self.creepster_1 = """
             ___/|\\___
            /          \\
           |    @      @ |
           /       ,<>.  \\
          |     __/ \\__  |
           \\      __    /
            |        |
            \\________/
        """

        self.creepster_2 = """
                 ___/|\\___
                /               \\
               |        @        @ |
               /         ,<>.         \\
              |       __/ \\__       |
               \\        __       /
                |          |
                \\____________/
        """

        self.creepster_3 = """
                     ___/|\\___
                    /                   \\
                   |            @            @ |
                   /             ,<>.             \\
                  |           __/ \\__           |
                   \\            __       /
                    |              |
                    \\________________/
        """

        self.creepster_4 = """
                         ___/|\\___
                        /                           \\
                       |                @                @ |
                       /                 ,<>.                 \\
                      |               __/ \\__               |
                       \\                __           /
                        |                  |
                        \\______________________/
        """

        self.creepster_5 = """
                                 ___/|\\___
                                /                                       \\
                               |                    @                    @ |
                               /                     ,<>.                     \\
                              |                   __/ \\__                   |
                               \\                    __               /
                                |                      |
                                \\__________________________________/
        """

        self.creepster_6 = """
                                         ___/|\\___
                                        /                                               \\
                                       |                            @                            @ |
                                       /                             ,<>.                             \\
                                      |                           __/ \\__                           |
                                       \\                            __                   /
                                        |                              |
                                        \\_________________________________________/
        """

        self.creepster_7 = """
                                                 ___/|\\___
                                                /                                                                   \\
                                               |                                        @                                        @ |
                                               /                                         ,<>.                                         \\
                                              |                                       __/ \\__                                       |
                                               \\                                        __                           /
                                                |                                          |
                                                \\________________________________________________________________/
        """

        self.smiley_1 = (
        """
            .''''''''.
         .'          '.
        /   @      @   \\
        :           `   :
        |               |
        :    .------.   :
         \\  '        '  /
          '.          .'
            '-......-'
        """
        )

        self.smiley_2 = (
        """
                .-''''''-.
             .'          '.
            /   @      @   \\
            :           `   :
            |               |
            :    .------.   :
             \\  '        '  /
              '.          .'
                '-......-'
        """
        )

        self.smiley_3 = (
        """
                        .-''''''-.
                     .'          '.
                    /   @      @   \\
                    :           `   :
                    |               |
                    :    .------.   :
                     \\  '        '  /
                      '.          .'
                        '-......-'
        """
        )

        self.smiley_4 = (
        """
                                         .-''''''-.
                                      .'          '.
                                     /   @      @   \\
                                     :           `   :
                                     |               |
                                     :    .------.   :
                                      \\  '        '  /
                                       '.          .'
                                         '-......-'
        """
        )

        self.smiley_5 = (
        """
                                                         .-''''''-.
                                                      .'          '.
                                                     /   @      @   \\
                                                     :           `   :
                                                     |               |
                                                     :    .------.   :
                                                      \\  '        '  /
                                                       '.          .'
                                                         '-......-'
        """
        )

        self.smiley_6 = (
        """
                                                                         .-''''''-.
                                                                      .'          '.
                                                                     /   @      @   \\
                                                                     :           `   :
                                                                     |               |
                                                                     :    .------.   :
                                                                      \\  '        '  /
                                                                       '.          .'
                                                                         '-......-'
        """
        )

        self.smiley_7 = (
        """
                                                                                 .-''''''-.
                                                                              .'          '.
                                                                             /   @      @   \\
                                                                             :           `   :
                                                                             |               |
                                                                             :    .------.   :
                                                                              \\  '        '  /
                                                                               '.          .'
                                                                                 '-......-'
        """
        )

        self.star_4_tabs = """
                    *
                   / \\
                  / * \\
                 / * * \\
                / * * * \\
                * * * * *
                \\ * * * /
                 \\ * * /
                  \\ * /
                   \\ /
                    *
        """
        self.star_3_tabs = """
                        *
                       / \\
                      / * \\
                     / * * \\
                    / * * * \\
                    * * * * *
                    \\ * * * /
                     \\ * * /
                      \\ * /
                       \\ /
                        *
        """
        self.cat = """
                                                                                     /\_/\  
                                                                                    ( o.o ) 
                                                                                     > ^ <
        """
        self.fish = """
        ><((((º> 
        """
        self.cat_with_fish_1 = """
    /\_/\\  
   ( o.o ) 
    > ^ < ><((((º>
       \\ \\\\
         ) )))))))))
        / /((()))))))
         (((()))))))))
           \\  ((((()))
        """

        self.cat_with_fish_2 = """
                   /\_/\\  
                  ( o.o ) 
                   > ^ < ><((((º>
                      \\ \\\\
                        ) )))))))))
                       / /((()))))))
                        (((()))))))))
                          \\  ((((()))
        """

        self.cat_with_fish_3 = """
                                 /\_/\\  
                                ( o.o ) 
                                 > ^ < ><((((º>
                                    \\ \\\\
                                      ) )))))))))
                                     / /((()))))))
                                      (((()))))))))
                                        \\  ((((()))
        """

        self.cat_with_fish_4 = """
                                               /\_/\\  
                                              ( o.o ) 
                                               > ^ < ><((((º>
                                                  \\ \\\\
                                                    ) )))))))))
                                                   / /((()))))))
                                                    (((()))))))))
                                                      \\  ((((()))
        """

        self.cat_with_fish_5 = """
                                                             /\_/\\  
                                                            ( o.o ) 
                                                             > ^ < ><((((º>
                                                                    \\ \\\\
                                                                      ) )))))))))
                                                                     / /((()))))))
                                                                      (((()))))))))
                                                                        \\  ((((()))
        """

        self.cat_with_fish_6 = """
                                                                     /\_/\\  
                                                                    ( o.o ) 
                                                                     > ^ < ><((((º>
                                                                            \\ \\\\
                                                                              ) )))))))))
                                                                             / /((()))))))
                                                                              (((()))))))))
                                                                                \\  ((((()))
        """

        self.cat_with_fish_7 = """
                                                                                 /\_/\\  
                                                                                ( o.o ) 
                                                                                 > ^ <
                                                                                    \\ \\\\
                                                                                      ) )))))))))
                                                                                     / /((()))))))
                                                                                      (((()))))))))
                                                                                        \\  ((((()))
        """

        self.catfish_1 = """
    /\_/\\  
   ( o.o ) 
    > ^ < ><((((º>
      ><(((º>
    """

        self.catfish_2 = """
                   /\_/\\  
                  ( o.o ) 
                   > ^ < ><((((º>
                     ><(((º>
        """

        self.catfish_3 = """
                                 /\_/\\  
                                ( o.o ) 
                                 > ^ < ><((((º>
                                   ><(((º>
        """

        self.catfish_4 = """
                                               /\_/\\  
                                              ( o.o ) 
                                               > ^ < ><((((º>
                                                 ><(((º>
        """

        self.catfish_5 = """
                                                             /\_/\\  
                                                            ( o.o ) 
                                                             > ^ < ><((((º>
                                                               ><(((º>
        """

        self.catfish_6 = """
                                                                         /\_/\\  
                                                                        ( o.o ) 
                                                                         > ^ < ><((((º>
                                                                           ><(((º>
        """

        self.catfish_7 = """
                                                                                 /\_/\\  
                                                                                ( o.o ) 
                                                                                 > ^ < ><((((º>
                                                                                   ><(((º>
        """


        self.smiley_face = '''
           .-""""""-.
          .'          '.
         /   O      O   \\
        |      (_)      |
        |  \  ______  /  |
         \  '.___.'  /
          '._______.'
        '''
        self.shades_0 = """
        (⌐■_■)
        """
        self.shades_1 = """
            (⌐■_■)
        """
        self.shades_2 = """
                (⌐■_■)
        """
        self.shades_3 = """
                    (⌐■_■)
        """
        self.shades_4 = """
                        (⌐■_■)
        """
        self.shades_5 = """
                            (⌐■_■)
        """
        self.shades_6 = """
                                (⌐■_■)
        """
        self.shades_7 = """
                                   (⌐■_■)
        """
        self.primary_patterns = [
            [
                self.smiley_1,
                self.smiley_2,
                self.smiley_3,
                self.smiley_4,
                self.smiley_5,
                self.smiley_6,
                self.smiley_7,
                self.smiley_6,
                self.smiley_5,
                self.smiley_4,
                self.smiley_3,
                self.smiley_2,
                self.smiley_1,
            ],
            [
                self.creepster_1,
                self.creepster_2,
                self.creepster_3,
                self.creepster_4,
                self.creepster_5,
                self.creepster_6,
                self.creepster_7,
                self.creepster_6,
                self.creepster_5,
                self.creepster_4,
                self.creepster_3,
                self.creepster_2,
                self.creepster_1,
            ],
            [
                self.shades_0,
                self.shades_1,
                self.shades_2,
                self.shades_3,
                self.shades_4,
                self.shades_5,
                self.shades_6,
                self.shades_7,
                self.shades_7,
                self.shades_6,
                self.shades_5,
                self.shades_4,
                self.shades_3,
                self.shades_2,
                self.shades_1,
                self.shades_0,
            ],
            [
                self.cat_with_fish_1,
                self.cat_with_fish_2,
                self.cat_with_fish_3,
                self.cat_with_fish_4,
                self.cat_with_fish_5,
                self.cat_with_fish_6,
                self.cat_with_fish_7,
                self.cat_with_fish_6,
                self.cat_with_fish_5,
                self.cat_with_fish_4,
                self.cat_with_fish_3,
                self.cat_with_fish_2,
                self.cat_with_fish_1
            ],
            [
                self.catfish_1,
                self.catfish_2,
                self.catfish_3,
                self.catfish_4,
                self.catfish_5,
                self.catfish_6,
                self.catfish_7,
                self.catfish_6,
                self.catfish_5,
                self.catfish_4,
                self.catfish_3,
                self.catfish_2,
                self.catfish_1
            ]
        ]
        self.secondary_patterns = [
            [
                self.smiley_face,
                self.smiley_6,
                self.smiley_face,
                self.smiley_6
            ],
            [ 
                self.fish, 
                self.cat, 
                self.fish, 
                self.cat, 
                self.fish,
                self.cat
            ],
            [
                self.star_4_tabs, 
                self.star_3_tabs, 
                self.star_4_tabs, 
                self.star_3_tabs
            ]
        ]

    def print_section(self, dict):
        now = datetime.datetime.now()
        try:
            title = dict["title"]
            section = dict["section"]
            lyrics = dict["lyrics"]
            duration = dict["duration"]
        except KeyError as e:
            print(f"dict missing key: {dict}")
            print(e)
            exit()

        string = f"{now}: [ {title} <{section}> {{ {duration} }} {{ {lyrics} }}] {dict}"
        print(string)

    def print_pattern(self, dict):
        random_item = self.generate_random_patterns(self.primary_patterns)
        pattern_count = 10
        one_third = pattern_count // 3
        two_thirds = 2 * (pattern_count // 3)

        primary_patterns_percentage = 0.4
        secondary_patterns_percentage = 0.2

        primary_patterns_count = int(pattern_count * primary_patterns_percentage)
        secondary_patterns_count = int(pattern_count * secondary_patterns_percentage)

        section_duration = dict["duration"]
        for i in range(pattern_count):
            if self.time_elapsed_for_current_section >= section_duration:
                break
            if i < primary_patterns_count:
                random_item = self.generate_random_patterns(self.primary_patterns)
            elif i < primary_patterns_count + secondary_patterns_count:
                random_item = self.generate_random_patterns(self.secondary_patterns)
            else:
                random_item = self.generate_random_patterns(self.primary_patterns)
            self.time_elapsed_for_current_section += self.print_items_in_list(random_item, section_duration)
        self.patterns_index += 1


    def print_items_in_list(self, list, section_duration):
        sleep_time = 0.2
        for i in list:
            if self.time_elapsed_for_current_section >= section_duration:
                break
            print(i)
            time.sleep(sleep_time)
            self.time_elapsed_for_current_section += datetime.timedelta(seconds=sleep_time)
        time_elapsed = datetime.timedelta(seconds=(len(list) * sleep_time))
        return time_elapsed

    def generate_random_patterns(self, pattern_set):
        return random.choice(pattern_set)
    
    def reset_elapsed_time(self):
        self.time_elapsed_for_current_section = datetime.timedelta(seconds=0)

    def start(self):
        for dict in self.song_dicts:
            try:
                duration = dict["duration"]
            except KeyError as e:
                print(f"dict missing key: {dict}")
                print(e)
                exit()
            self.reset_elapsed_time()
            start_time = datetime.datetime.now()
            while datetime.datetime.now() - start_time <= duration:
                if dict["lyrics"]:
                    self.print_section(dict)
                else:
                    self.print_pattern(dict)


song_dicts = [
    {
        "title": "Song title",
        "section": "Intro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=15.584)
    },
    {
        "title": "Song title",
        "section": "Verse 1",
        "lyrics": "House with no walls. With a beach-front price. Starting to think a small town would feel nice.",
        "duration": datetime.timedelta(seconds=24.935)
    },
    {
        "title": "Song title",
        "section": "Chorus 1",
        "lyrics": "Honeyed up by power chords and echo. Honeyed up by power chords and echo. Chills from head to toe. Honeyed up by power chords and echo.",
        "duration": datetime.timedelta(seconds=12.468)
    },
    {
        "title": "Song title",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=12.468)
    },
    {
        "title": "Song title",
        "section": "Verse 2",
        "lyrics": "Angels singing above my windows playing with the shame of broken customs. Trouble is close and its carrying on. Praying with the saints so we all get along.",
        "duration": datetime.timedelta(seconds=24.936)
    },
    {
        "title": "Song title",
        "section": "Chorus 2",
        "lyrics": "Honeyed up by power chords and echo. Honeyed up by power chords and echo. Chills from head to toe. Honeyed up by power chords and echo. Good god I must miss my faith. Dumbfounded in a dark, loud space. Chills from head to toe. Honeyed up by power chords and echo.",
        "duration": datetime.timedelta(seconds=24.936)
    },
    {
        "title": "Song title",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=12.468)
    },
    {
        "title": "Song title",
        "section": "Verse 3",
        "lyrics": "Less screaming on stages more embracing quiet trends. I'm in a season of crying in front of friends.",
        "duration": datetime.timedelta(seconds=12.468)
    },
    {
        "title": "Song title",
        "section": "Chorus 3",
        "lyrics": "Honeyed up by power chords and echo. Honeyed up by power chords and echo. Chills from head to toe. Honeyed up by power chords and echo. Good god I must miss my faith. Dumbfounded in a dark, loud space. Chills from head to toe. Honeyed up by power chords and echo.",
        "duration": datetime.timedelta(seconds=24.936)
    },
    {
        "title": "Song title",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=18.702)
    },
    {
        "title": "Song title",
        "section": "Outro",
        "lyrics": "Less screaming on stages more embracing quiet trends.",
        "duration": datetime.timedelta(seconds=18.702)
    },
    {
        "title": "Song title",
        "section": "Outro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=12.468)
    },
]


peoplea = [
 {
        "title": "Peoplea Potluck",
        "section": "Intro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=15.584)
    },
    # {
    #     "title": "Peoplea Potluck",
    #     "section": "Verse 1",
    #     "lyrics": """In the heart of Tucker, under stars aglow,
    #     Peoplea gathered 'round, a festive, loving show.
    #     Each dish, a tale, a memory shared,
    #     A potluck feast, our bond declared.""",
    #     "duration": datetime.timedelta(seconds=24.935)
    # },
    # {
    #     "title": "Peoplea Potluck",
    #     "section": "Chorus 1",
    #     "lyrics": """Oh, Peoplea, our circle tight,
    #     Through laughter, tears, and starry night.
    #     Together, we'll stand, through joy and cheer,
    #     Our hearts entwined, year after year.""",
    #     "duration": datetime.timedelta(seconds=12.468)
    # },
    {
        "title": "Peoplea Potluck",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=12.468)
    },
    # {
    #     "title": "Peoplea Potluck",
    #     "section": "Verse 2",
    #     "lyrics": """Sophie's laughter, a beacon bright,
    #     Zach's woodwork, a wondrous sight.
    #     Callie's flair and Mike's bass hum,
    #     Lindsay's baking, Will's wisdom.""",
    #     "duration": datetime.timedelta(seconds=24.936)
    # },
    # {
    #     "title": "Peoplea Potluck",
    #     "section": "Chorus 2",
    #     "lyrics": """Oh, Peoplea, our circle tight,
    #     Through laughter, tears, and starry night.
    #     Together, we'll stand, through joy and cheer,
    #     Our hearts entwined, year after year.""",
    #     "duration": datetime.timedelta(seconds=24.936)
    # },
    {
        "title": "Peoplea Potluck",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=12.468)
    },
    # {
    #     "title": "Peoplea Potluck",
    #     "section": "Bridge",
    #     "lyrics": """Through seasons' change and passing time,
    #     Our bond grows strong, a cherished rhyme.
    #     The Christmas potluck, a tradition born,
    #     In love and support, we're forever sworn.""",
    #     "duration": datetime.timedelta(seconds=12.468)
    # },
    # {
    #     "title": "Peoplea Potluck",
    #     "section": "Chorus 3",
    #     "lyrics": """Oh, Peoplea, our circle tight,
    #     Through laughter, tears, and starry night.
    #     Together, we'll stand, through joy and cheer,
    #     Our hearts entwined, year after year.""",        
    #     "duration": datetime.timedelta(seconds=24.936)
    # },
    {
        "title": "Peoplea Potluck",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=18.702)
    },
    {
        "title": "Peoplea Potluck",
        "section": "Outro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=18.702)
    },
    {
        "title": "Peoplea Potluck",
        "section": "Outro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=12.468)
    },
]

shortened_song_dicts = [
    {
        "title": "Song title",
        "section": "Intro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=10)
    },
    {
        "title": "Song title",
        "section": "Verse 1",
        "lyrics": "House with no walls. With a beach-front price. Starting to think a small town would feel nice.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Chorus 1",
        "lyrics": "Honeyed up by power chords and echo. Honeyed up by power chords and echo. Chills from head to toe. Honeyed up by power chords and echo.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=10)
    },
    {
        "title": "Song title",
        "section": "Verse 2",
        "lyrics": "Angels singing above my windows playing with the shame of broken customs. Trouble is close and its carrying on. Praying with the saints so we all get along.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Chorus 2",
        "lyrics": "Honeyed up by power chords and echo. Honeyed up by power chords and echo. Chills from head to toe. Honeyed up by power chords and echo. Good god I must miss my faith. Dumbfounded in a dark, loud space. Chills from head to toe. Honeyed up by power chords and echo.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=10)
    },
    {
        "title": "Song title",
        "section": "Verse 3",
        "lyrics": "Less screaming on stages more embracing quiet trends. I'm in a season of crying in front of friends.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Chorus 3",
        "lyrics": "Honeyed up by power chords and echo. Honeyed up by power chords and echo. Chills from head to toe. Honeyed up by power chords and echo. Good god I must miss my faith. Dumbfounded in a dark, loud space. Chills from head to toe. Honeyed up by power chords and echo.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Interlude",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=10)
    },
    {
        "title": "Song title",
        "section": "Outro",
        "lyrics": "Less screaming on stages more embracing quiet trends.",
        "duration": datetime.timedelta(seconds=5)
    },
    {
        "title": "Song title",
        "section": "Outro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=10)
    },
]

just_patterns = [
    {
        "title": "Song title",
        "section": "Intro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=1000)
    }
]

five_seconds = [
    {
        "title": "Song title",
        "section": "Intro",
        "lyrics": None,
        "duration": datetime.timedelta(seconds=3)
    },
    {
        "title": "Gmail Reply Bot",
        "section": "V1",
        "lyrics": "Monitoring time",
        "duration": datetime.timedelta(seconds=2)
    }
]

# LyricPrinter(shortened_song_dicts).start()
# LyricPrinter(peoplea).start()


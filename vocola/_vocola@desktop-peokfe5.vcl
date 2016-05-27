# Global voice commands on desktop

# Desktop navigation
Downward                              = { Down_20 };
Upward                                = { Up_20 };

# Basic text navigation
Shup                                  = {Shift+Up};

Shab                                  = {Shift+Tab};

Dunk                                  = {Enter};

D dunk                                = { Enter_2 };
T dunk                                = { Enter_3 };
Mup                                   = {Up};

Dup                                   = {Down};

E line                                = {End};

Del line                              = {End} {Shift + Home} {Del};
C line                                = {End} {Shift + Home};


Bo line                               = {Home};
Seco line                             = { End } ';';                    # Semicolon at end of line
Reco line                             = { End } ':';
Cleft                                 = { Ctrl + Left };
Cleft 1..99                           = { Ctrl + Left_$1 };
Crait                                 = { Ctrl + Right };
Crait 1..99                           = { Ctrl + Right_$1 };
Fithi                                 = { Ctrl + f };

# Killing and yanking and stuff

Kill                                  = {Ctrl+x};

Yank                                  = {Ctrl+v};

Steal                                 = {Ctrl+c};

Crap                                  = {Ctrl+z};

S kill                                = {Home} {Shift+End} {Ctrl+x};

D Kill                                = {Home} {Shift+Down} {Shift+End} {Ctrl+x};

T Kill                                = {Home}{Shift+Down} {Shift+Down} {Shift+End} {Ctrl+x};

Overkill                              = {Home}{Shift+Down} {Shift+Down} {Shift+Down} {Shift+End} {Ctrl+x};

Del 1..99 next                        = {Ctrl + Right_$1} {Ctrl + Backspace_$1};
Del 1..99 last                        = {Ctrl + Backspace_$1};
Sanno                                 = { Ctrl + s };




# General formatting

Indent                                = {Space_4};
Prain                                 = '(  )' {Left_2};
Krax                                  = '{}' {Left};
Brax                                  = '[]' {Left};
Squotes                               = "'  '" { Left_2 };
Duotes                                = '"  "' { Left_2 }; 

# Bash commands
Chadirr                               = {c} {d} {Space};
Ellis                                 = {l} {s} { Space };
Tilde                                 = '~';
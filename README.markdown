# Mega Man X6 Tweaker

[acediez] developed some amazing [Mega Man X6 tweaks].
He also released a [data file] documenting the tweaks
and a [graphical patching utility] that lets players customize Mega Man X6.

This Python 3 script implements a command-line tweaking tool for Mega Man X6.
Currently, it has the following features:

 - Verify integrity of the game image prior to patching
 - Edit hunter ranks
   - Souls required
   - Normal and limited parts allowed

## How to use

    x6tweaks x6.bin < tweaks.json

The program receives via standard input JSON-formatted data specifying the tweaks that are to be applied. The `examples.json` file contains the game's own default values; applying those tweaks will result in an unmodified game image. The file may be copied and customized to the player's liking.

[acediez]: http://www.romhacking.net/forum/index.php?action=profile;u=67963
[Mega Man X6 tweaks]: http://www.romhacking.net/forum/index.php?topic=26507
[data file]: http://www.romhacking.net/documents/780/
[graphical patching utility]: http://www.romhacking.net/utilities/1414/

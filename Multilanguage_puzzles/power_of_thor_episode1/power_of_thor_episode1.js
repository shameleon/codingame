var inputs = readline().split(' ');
const lightX = parseInt(inputs[0]); // the X position of the light of power
const lightY = parseInt(inputs[1]); // the Y position of the light of power
const initialTx = parseInt(inputs[2]); // Thor's starting X position
const initialTy = parseInt(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
    const remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.

    // Write an action using console.log()
    // console.error('Debug messages...');
    let ans = "";
    let delta_y = (inputs[1] - inputs[3]);
    if (delta_y > 0)
    {
        ans += "S";
        inputs[3]++;
    }
    else if (delta_y < 0)
    {
        ans += "N";
        inputs[3]--;
    }
    let delta_x = (inputs[0] - inputs[2]);
    if (delta_x > 0)
    {
        ans += "E";
        inputs[2]++;
    }
    else if (delta_x < 0)
    {
        ans += "W";
        inputs[2]--;
    }
    // A single line providing the move to be made: N NE E SE S SW W or NW
    console.log(ans);
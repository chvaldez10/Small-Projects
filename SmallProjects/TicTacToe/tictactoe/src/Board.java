public class Board implements Constants{
    private char tictacBoard[][];
    private int markCount;

    public Board() {
        markCount = 0;
        tictacBoard = new char[3][];

        for(int i=0; i<3; i++) {
            tictacBoard[i] = new char[3];
            for (int j=0; j<3; j++)
                tictacBoard[i][j] = spaceChar;
        }
    }

    public char getMark(int row, int col) {
        return tictacBoard[row][col];
    }

    public boolean isFull() {
        return markCount == 9;
    }

    public boolean xWins() {
        if(checkWinner(lettterX) == 1) {
            return true;
        } else
            return false;
    }

    public boolean oWins() {
        if(checkWinner(letterO)==1)
            return true;
        else
            return false;
    }

    public int checkWinner(char mark) {
        //check rows
        for (int row=0; row<3; row++) {
            if(tictacBoard[row][0]==mark && tictacBoard[row][1]==mark &
                    tictacBoard[row][2] == mark) return 1;
        }

        //check columns
        for (int col=0; col<3; col++) {
            if(tictacBoard[0][col]==mark && tictacBoard[1][col]==mark &
                    tictacBoard[2][col] == mark) return 1;
        }
        
        if ((tictacBoard[0][0] == mark && tictacBoard[1][1] == mark && tictacBoard[2][2] == mark) ||
                (tictacBoard[0][2] == mark && tictacBoard[1][1] == mark && tictacBoard[2][0] == mark))
            return 1;

        return 0;
    }

    public void addMark(int row, int col, char mark) {
        tictacBoard[row][col] = mark;
        markCount++;
    }

    /**
     * displays the game board to the console.
     */
    public void display() {
        displayColumnHeaders();
        addHyphens();
        for(int row=0; row<3; row++) {
            addSpaces();
            System.out.println("    row " + row + " ");
            for (int col = 0; col < 3; col++)
                System.out.print("|  " + getMark(row, col) + "  ");
            System.out.println("|");
            addSpaces();
            addHyphens();
        }
    }

    /**
     * clears game board
     */
    public void clear() {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                tictacBoard[i][j] = spaceChar;
        markCount = 0;
    }

    /**
     * displays column numbers on game board
     */
    void displayColumnHeaders() {
        System.out.print("          ");
        for (int j = 0; j < 3; j++)
            System.out.print("|col " + j);
        System.out.println();
    }

    /**
     * row separators
     */
    void addHyphens() {
        System.out.print("          ");
        for (int j = 0; j < 3; j++)
            System.out.print("+-----");
        System.out.println("+");
    }

    /**
     * column separators
     */
    void addSpaces() {
        System.out.print("          ");
        for (int j = 0; j < 3; j++)
            System.out.print("|     ");
        System.out.println("|");
    }
}

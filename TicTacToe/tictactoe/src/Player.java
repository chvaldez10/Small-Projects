import java.util.Scanner;

public class Player {
    protected String name;
    protected Board board;
    protected Player opponent;
    protected char mark;

    public Player() {
        this.name = "no name";
        this.board = new Board();
        this.opponent = null;
        this.mark = 'z';
    }

    public Player(String playerName, char playerMark) {
        this.name = playerName;
        this.mark = playerMark;
    }

    public void setBoard(Board board){
        this.board = board;
    }

    public Board getBoard(){
        return this.board;
    }

    public void setOpponent(Player player) {
        this.opponent = player;
    }

    public void play() {
        if(!this.board.xWins() && !this.board.oWins() && !this.board.isFull()) {
            makeMove();
        }
    }

    public void makeMove() {
        int row, col;

        Scanner scan = new Scanner(System.in);
        System.out.println(this.name + "'s turn!");
        System.out.println("Enter the row you want to place your marker " + this.mark + ":");
        row = scan.nextInt();
        System.out.println("Enter the column you want to place your marker " + this.mark + ":");
        col = scan.nextInt();
        this.board.addMark(row, col, mark);
    }
}

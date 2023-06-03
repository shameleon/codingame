#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <stack>
#include <vector>

static int ReadInt() {
    int val;
    std::cin >> val;
    return val;
}

static int ReadIntIgnore() {
    int val;
    std::cin >> val;
    std::cin.ignore();
    return val;
}

// Interpreter for the Brainfuck esoteric language.
class Interpreter {
public:
    using Cells          = std::vector<uint8_t>;
    using Cell           = Cells::value_type;
    using ProgramLines   = std::vector<std::string>;
    using InstructionPtr = std::string::const_iterator;

    explicit Interpreter(int num_cells, ProgramLines&& lines)
        : m_cells(num_cells),
          m_cell_ptr(m_cells.data()),
          m_lines(std::move(lines)) {}

    void Run() {
        // Can't run anything without code.
        if (m_lines.empty()) {
            return;
        }

        // Ensure all jumps are well-formed within the code before executing it.
        if (!SanitizeJumps()) {
            SyntaxError();
            return;
        }

        for (const auto& line : m_lines) {
            auto inst_ptr = line.cbegin();

            while (inst_ptr != line.cend()) {
                if (m_stop_execution) {
                    return;
                }

                switch (*inst_ptr) {
                case '<':
                    HandlePointerDecrement();
                    break;
                case '>':
                    HandlePointerIncrement();
                    break;
                case '-':
                    HandleDecrementPointedToCell();
                    break;
                case '+':
                    HandleIncrementPointedToCell();
                    break;
                case '.':
                    HandleReadASCII();
                    break;
                case ',':
                    HandleAcceptInput();
                    break;
                case '[':
                    {
                        m_jump_stack.push(inst_ptr);
                        if (*m_cell_ptr == 0) {
                            auto start_inst_ptr = inst_ptr;

                            while (++inst_ptr != line.cend()) {
                                if (*inst_ptr == '[') {
                                    m_jump_stack.push(inst_ptr);
                                } else if (*inst_ptr == ']') {
                                    const auto temp_ptr = m_jump_stack.top();
                                    m_jump_stack.pop();
                                    if (start_inst_ptr == temp_ptr) {
                                        break;
                                    }
                                }
                            }
                        }
                    }
                    break;
                case ']':
                    {
                        if (*m_cell_ptr == 0) {
                            m_jump_stack.pop();
                        } else {
                            inst_ptr = m_jump_stack.top();
                        }
                    }
                    break;
                }

                inst_ptr++;
            }
        }
    }

private:
    // Handles the behavior of the '<' operator.
    void HandlePointerDecrement() {
        if (!IsPointerDecrementValid()) {
            PointerOutOfBounds();
            return;
        }

        --m_cell_ptr;
    }

    // Handles the behavior of the '>' operator.
    void HandlePointerIncrement() {
        if (!IsPointerIncrementValid()) {
            PointerOutOfBounds();
            return;
        }

        ++m_cell_ptr;
    }

    // Handles the behavior of the '-' operator
    void HandleDecrementPointedToCell() {
        const auto dec = static_cast<Cell>(*m_cell_ptr - 1);
        if (dec == std::numeric_limits<Cell>::max()) {
            // Underflow
            IncorrectValue();
            return;
        }
        *m_cell_ptr = dec;
    }

    // Handles the behavior of the '+' operator
    void HandleIncrementPointedToCell() {
        const auto inc = static_cast<Cell>(*m_cell_ptr + 1);
        if (inc == 0) {
            // Overflow
            IncorrectValue();
            return;
        }
        *m_cell_ptr = inc;
    }

    // Handles the behavior of the '.' operator.
    void HandleReadASCII() const {
        std::cout << static_cast<char>(*m_cell_ptr);
    }

    // Handles the behavior of the ',' operator.
    void HandleAcceptInput() {
        const auto value = ReadIntIgnore();
        if (value < 0 || value > 255) {
            IncorrectValue();
            return;
        }
        *m_cell_ptr = static_cast<Cell>(value);
    }

    // Handles the behavior of the '[' and ']' operator.
    void HandleJump(InstructionPtr ptr) {

    }

    // Utility functions

    // Ensure all '[' operators have a matching ']' operator.
    bool SanitizeJumps() const {
        int pairs_left_open = 0;

        for (const auto& line : m_lines) {
            for (const char c : line) {
                if (c == '[') {
                    ++pairs_left_open;
                } else if (c == ']') {
                    --pairs_left_open;
                }
            }
        }

        return pairs_left_open == 0;
    }


    void IncorrectValue() {
        std::cout << "INCORRECT VALUE" << std::endl;
        m_stop_execution = true;
    }

    void PointerOutOfBounds() {
        std::cout << "POINTER OUT OF BOUNDS" << std::endl;
        m_stop_execution = true;
    }

    void SyntaxError() {
        std::cout << "SYNTAX ERROR" << std::endl;
        m_stop_execution = true;
    }

    bool IsPointerDecrementValid() const {
        return m_cell_ptr != &m_cells.front();
    }

    bool IsPointerIncrementValid() const {
        return m_cell_ptr != &m_cells.back();
    }

    // Our storage of cells to place values into,
    // along with the pointer to the current cell.
    Cells m_cells;
    Cell* m_cell_ptr;

    // Stack and pointer for handling the conditional operators '[' and ']'
    std::stack<InstructionPtr> m_jump_stack;
    InstructionPtr m_instruction_ptr;

    // Whether or not execution needs to stop due to an error.
    bool m_stop_execution = false;

    // Code to run
    ProgramLines m_lines;
};

static Interpreter::ProgramLines ReadLines(int num_lines) {
    Interpreter::ProgramLines lines;
    lines.reserve(num_lines);

    for (int i = 0; i < num_lines; i++) {
        std::string r;
        std::getline(std::cin, r);
        lines.push_back(std::move(r));
    }

    return lines;
}

// With everything extracted out into a class,
// our main function is a tiny boi.

int main()
{
    const int L = ReadInt();
    const int S = ReadInt();
    const int N = ReadInt();
    std::cin.ignore();

    Interpreter interpreter(S, ReadLines(L));
    interpreter.Run();

    return 0;
}

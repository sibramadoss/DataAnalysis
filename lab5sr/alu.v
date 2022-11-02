module ALU (
    input logic [31:0] SrcA,
    input logic [31:0] SrcB,
    output logic [2:0] ALUControl,
    output logic [31:0] ALUResult
);
    always @ (*)
    begin
        case(ALUControl)
        3'b010:
            ALUResult = SrcA + SrcB;
        3'b110:
            ALUResult = SrcA - SrcB;
        default: ALUResult = SrcA + SrcB;
        endcase
    end

endmodule




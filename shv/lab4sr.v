module dff (
    input logic clk,
    input logic din,
    output logic q
);

always_ff @(posedge clk) begin
    q <= d    //blocking assignment
end

endmodule

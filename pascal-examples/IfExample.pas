program IfExample (input, output);
var x : integer;
begin
    write('Enter a number: ');
    read(x);
    if x > 0 then begin
        write('The number is greater than zero');
        writeln;
    end
end.
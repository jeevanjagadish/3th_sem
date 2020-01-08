declare
       num number;
       upper number;
       lower number;
  begin
        num:=&num;
        upper:=&upper;
        lower:=&lower;
       if(num>=upper AND num<=lower)
     then
         dbms_output.put_line('number is in the range');
     else
        dbms_output.put_line('number is not in the range');
     end if;
  end;
   /
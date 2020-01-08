declare
       num number;
       i number:=2;
       c number:=0;
  begin
        num:=&num;
       for i in 2..num
       loop
          if((mod(num,i))=0)
           then
              c:=c+1;
         end if;
      end loop;
     if(c>2)
     then
         dbms_output.put_line(num||' not a prime');
     else
        dbms_output.put_line(num||' is prime');
     end if;
  end;
   /
Q1 = "SELECT Student.Sname, Student.Sfamily, Student.city, College.clg_name FROM Student INNER JOIN College ON Student.#clg = College.#clg WHERE Student.city != College.city"
Q2 = "SELECT Proof.Pname, Proof.Pfamily FROM Proof INNER JOIN Sec INNER JOIN Course ON Proof.#P = Sec.#P and Course.#C = Sec.#C WHERE Course.Cname = 'database' and Sec.term = 1 and Sec.year = 1401"
Q3 = "SELECT Student.Sname, Student.Sfamily, Course.Cname FROM Student INNER JOIN Course INNER JOIN Sec ON Student.#S = Sec.#S and Sec.#C =Course.#C WHERE Course.#clg != Student.#clg"
Q4 = "SELECT Course.Cname, Course.Cunit, Sec.year, Sec.term, Sec.Score FROM Course INNER JOIN Student INNER JOIN Sec ON Student.#S = Sec.#S and Sec.#C =Course.#C WHERE Student.Sname = 'negar' and Student.Sfamily = 'afshar' and Sec.year <= 1401 and ((Sec.year, Sec.term) NOT IN (SELECT Course.Cname, Course.Cunit, Sec.year, Sec.term, Sec.Score FROM Course INNER JOIN Student INNER JOIN Sec ON Student.#S = Sec.#S and Sec.#C =Course.#C WHERE Student.Sname = 'negar' and Student.Sfamily = 'afshar' and Sec.year = 1401 and SEC.term = 2))"
Q5 = "SELECT Student.Sname, Student.Sfamily, Proof.Pname, Proof.Pfamily, College.clg_name, Course.Cname, Sec.Score FROM College INNER JOIN Student INNER JOIN Proof INNER JOIN Course INNER JOIN Sec ON Proof.P# = College.P# and Proof.P# = Sec.P# and Student.#S =Sec.#S and Student.#clg = College.#clg and Proof.#clg = College.#clg and Course.#clg = College.#clg andCourse.#C = Sec.#C WHERE Sec.Score < 10"
Q6 = "SELECT Course.Cname FROM College INNER JOIN Sec INNER JOIN Proof INNER JOIN Course ON Sec.#C = Course.#C and Sec.#clg = "
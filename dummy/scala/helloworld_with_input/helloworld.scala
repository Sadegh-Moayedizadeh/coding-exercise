import scala.io.StdIn.readLine

@main def helloWorld() = 
    println("print your name: ")
    val name = readLine()
    println(s"hello $name")

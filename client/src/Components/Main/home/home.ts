import { Component, ViewChild, ElementRef, AfterViewChecked } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.html',
  styleUrls: ['./home.css'],
})

export class Home implements AfterViewChecked {
  @ViewChild('messagesContainer') messagesContainer!: ElementRef;
  @ViewChild('inputBox') inputBox!: ElementRef;

  chat = [
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "agent", text: "It is not." },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "agent", text: "it is not." },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
    { role: "user", text: "I just broke up with him" },
    { role: "agent", text: "I'm so sorry for that" },
    { role: "user", text: "its my fault" },
  ];

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  private scrollToBottom(): void {
    const container = this.messagesContainer.nativeElement;
    container.scrollTop = container.scrollHeight;
  }

  
}
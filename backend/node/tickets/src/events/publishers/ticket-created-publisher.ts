import { Publisher, Subjects, TicketCreatedEvent } from '@scriptmotor/common';

export class TicketCreatedPublisher extends Publisher<TicketCreatedEvent> {
  subject: Subjects.TicketCreated = Subjects.TicketCreated;
}

import { Publisher, Subjects, TicketCreatedEvent } from '@scriptmotor/common';

export class TicketCreatedPublisher extends Publisher<TicketCreatedEvent> {
  readonly subject = Subjects.TicketCreated;
}

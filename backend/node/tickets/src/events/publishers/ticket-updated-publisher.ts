import { Publisher, Subjects, TicketUpdatedEvent } from '@scriptmotor/common';

export class TicketUpdatedPublisher extends Publisher<TicketUpdatedEvent> {
  subject: Subjects.TicketUpdated = Subjects.TicketUpdated;
}

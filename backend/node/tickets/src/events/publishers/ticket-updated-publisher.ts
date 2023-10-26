import { Publisher, Subjects, TicketUpdatedEvent } from '@scriptmotor/common';

export class TicketUpdatedPublisher extends Publisher<TicketUpdatedEvent> {
  readonly subject = Subjects.TicketUpdated;
}
